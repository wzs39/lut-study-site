#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zero-dependency incremental uploader for Cloudflare R2 (S3-compatible SigV4).

Reads R2 credentials exclusively from environment variables (never hardcoded):
    R2_ACCOUNT_ID          Cloudflare Account ID (32-char hex)
    R2_ACCESS_KEY_ID       R2 S3 API Access Key ID
    R2_SECRET_ACCESS_KEY   R2 S3 API Secret Access Key
    R2_BUCKET              Target R2 bucket name

Usage:
    # Preview what will be uploaded (excluding personal Submissions/CV files)
    python tools/sync_r2.py --dry-run

    # Upload all 820 public courseware files incrementally to gs/r2 prefix `courseware/`
    python tools/sync_r2.py

    # Also write public R2 base URL into assets/config.js after sync
    python tools/sync_r2.py --write-config https://pub-xxxx.r2.dev/courseware
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import datetime
import hashlib
import hmac
import mimetypes
import os
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

TOOLS_DIR = Path(__file__).resolve().parent
SITE_ROOT = TOOLS_DIR.parent
sys.path.insert(0, str(TOOLS_DIR))
import build_courseware_index as indexer  # noqa: E402

EXTRA_MIME = {
    ".pdf": "application/pdf",
    ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    ".ppt": "application/vnd.ms-powerpoint",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".doc": "application/msword",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".csv": "text/csv; charset=utf-8",
    ".md": "text/markdown; charset=utf-8",
    ".txt": "text/plain; charset=utf-8",
    ".py": "text/plain; charset=utf-8",
    ".ipynb": "application/json; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".mp3": "audio/mpeg",
    ".wav": "audio/wav",
    ".m4a": "audio/mp4",
    ".mp4": "video/mp4",
    ".webm": "video/webm",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
    ".gif": "image/gif",
    ".svg": "image/svg+xml",
    ".zip": "application/zip",
}


def guess_content_type(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in EXTRA_MIME:
        return EXTRA_MIME[ext]
    guessed, _ = mimetypes.guess_type(path.name)
    return guessed or "application/octet-stream"


def aws_encode(value: str, safe: str = "-_.~") -> str:
    return urllib.parse.quote(value, safe=safe)


def _sign(key: bytes, msg: str) -> bytes:
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def sign_v4_headers(
    method: str,
    host: str,
    canonical_uri: str,
    query_params: dict[str, str],
    extra_headers: dict[str, str],
    payload_sha256: str,
    access_key: str,
    secret_key: str,
    region: str = "auto",
    service: str = "s3",
    now: datetime.datetime | None = None,
) -> dict[str, str]:
    now = now or datetime.datetime.now(datetime.timezone.utc)
    amz_date = now.strftime("%Y%m%dT%H%M%SZ")
    date_stamp = now.strftime("%Y%m%d")

    headers = {
        "host": host,
        "x-amz-content-sha256": payload_sha256,
        "x-amz-date": amz_date,
    }
    for k, v in extra_headers.items():
        headers[k.lower()] = " ".join(str(v).strip().split())

    sorted_keys = sorted(headers.keys())
    canonical_headers = "".join(f"{k}:{headers[k]}\n" for k in sorted_keys)
    signed_headers = ";".join(sorted_keys)

    canonical_query = "&".join(
        f"{aws_encode(k)}={aws_encode(v)}" for k, v in sorted(query_params.items())
    )
    canonical_request = "\n".join(
        [method, canonical_uri, canonical_query, canonical_headers, signed_headers, payload_sha256]
    )
    credential_scope = f"{date_stamp}/{region}/{service}/aws4_request"
    string_to_sign = "\n".join(
        [
            "AWS4-HMAC-SHA256",
            amz_date,
            credential_scope,
            hashlib.sha256(canonical_request.encode("utf-8")).hexdigest(),
        ]
    )

    k_date = _sign(("AWS4" + secret_key).encode("utf-8"), date_stamp)
    k_region = _sign(k_date, region)
    k_service = _sign(k_region, service)
    k_signing = _sign(k_service, "aws4_request")
    signature = hmac.new(k_signing, string_to_sign.encode("utf-8"), hashlib.sha256).hexdigest()

    auth = (
        f"AWS4-HMAC-SHA256 Credential={access_key}/{credential_scope}, "
        f"SignedHeaders={signed_headers}, Signature={signature}"
    )
    out = dict(headers)
    out["authorization"] = auth
    return out


class R2Client:
    def __init__(self, account_id: str, access_key: str, secret_key: str, bucket: str):
        self.host = f"{account_id.strip()}.r2.cloudflarestorage.com"
        self.access_key = access_key.strip()
        self.secret_key = secret_key.strip()
        self.bucket = bucket.strip()

    def _request(
        self,
        method: str,
        key: str = "",
        query: dict[str, str] | None = None,
        body: bytes = b"",
        extra_headers: dict[str, str] | None = None,
        timeout: int = 120,
    ) -> bytes:
        query = query or {}
        extra_headers = extra_headers or {}
        canonical_uri = "/" + aws_encode(self.bucket)
        if key:
            canonical_uri += "/" + "/".join(aws_encode(seg) for seg in key.split("/"))
        payload_hash = hashlib.sha256(body).hexdigest()
        signed = sign_v4_headers(
            method=method,
            host=self.host,
            canonical_uri=canonical_uri,
            query_params=query,
            extra_headers=extra_headers,
            payload_sha256=payload_hash,
            access_key=self.access_key,
            secret_key=self.secret_key,
        )
        qs = "&".join(f"{aws_encode(k)}={aws_encode(v)}" for k, v in sorted(query.items()))
        url = f"https://{self.host}{canonical_uri}" + (f"?{qs}" if qs else "")
        last_err: Exception | None = None
        for attempt in range(1, 5):
            req = urllib.request.Request(url, data=body if method == "PUT" else None, method=method)
            for k, v in signed.items():
                if k != "host":
                    req.add_header(k, v)
            try:
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    return resp.read()
            except urllib.error.HTTPError as exc:
                if exc.code >= 500 or exc.code == 429:
                    last_err = exc
                    if attempt < 4:
                        time.sleep(attempt * 1.5)
                        continue
                detail = ""
                try:
                    detail = exc.read().decode("utf-8", errors="replace")[:300]
                except Exception:
                    pass
                raise RuntimeError(f"HTTP {exc.code} on {method} {canonical_uri}: {detail}") from exc
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                last_err = exc
                if attempt < 4:
                    time.sleep(attempt * 1.5)
        raise RuntimeError(f"Request failed for {method} {canonical_uri}: {last_err}")

    def list_etags(self, prefix: str) -> dict[str, str]:
        etags: dict[str, str] = {}
        token = ""
        while True:
            query = {"list-type": "2", "prefix": prefix}
            if token:
                query["continuation-token"] = token
            raw = self._request("GET", key="", query=query, timeout=30)
            root = ET.fromstring(raw)
            ns = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}
            for node in root.findall("s3:Contents", ns):
                k = node.findtext("s3:Key", default="", namespaces=ns)
                e = node.findtext("s3:ETag", default="", namespaces=ns).strip('"')
                if k:
                    etags[k] = e
            if root.findtext("s3:IsTruncated", default="false", namespaces=ns).lower() != "true":
                break
            token = root.findtext("s3:NextContinuationToken", default="", namespaces=ns)
            if not token:
                break
        return etags

    def put_file(self, key: str, path: Path) -> None:
        data = path.read_bytes()
        headers = {
            "content-type": guess_content_type(path),
            "cache-control": "public, max-age=86400",
        }
        last_err: Exception | None = None
        for attempt in range(1, 4):
            try:
                self._request("PUT", key=key, body=data, extra_headers=headers, timeout=180)
                return
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                last_err = exc
                if attempt < 3:
                    time.sleep(attempt * 1.5)
        raise RuntimeError(f"Upload failed for {key}: {last_err}")


def md5_hex(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def update_config_js(public_base_url: str) -> None:
    clean = public_base_url.strip().rstrip("/")
    parsed = urllib.parse.urlsplit(clean)
    if parsed.scheme != "https" or not parsed.netloc or parsed.query or parsed.fragment:
        raise ValueError("Public base URL must be a clean https:// URL without query/fragment")
    cfg = SITE_ROOT / "assets" / "config.js"
    text = cfg.read_text(encoding="utf-8")
    updated, n = re.subn(
        r'coursewareBaseUrl:\s*"[^"]*"',
        f'coursewareBaseUrl: "{clean}"',
        text,
        count=1,
    )
    if n != 1:
        raise RuntimeError("Could not locate coursewareBaseUrl in assets/config.js")
    cfg.write_text(updated, encoding="utf-8", newline="\n")
    print(f"Updated assets/config.js -> coursewareBaseUrl: \"{clean}\"")


def main() -> None:
    parser = argparse.ArgumentParser(description="Incremental Cloudflare R2 sync for LUT courseware.")
    parser.add_argument("--prefix", default="courseware", help="Key prefix inside the R2 bucket (default: courseware)")
    parser.add_argument("--workers", type=int, default=6, help="Concurrent upload workers (default: 6)")
    parser.add_argument("--dry-run", action="store_true", help="Show upload plan without writing to R2")
    parser.add_argument("--max-total-gb", type=float, default=9.0, help="Hard safety cap in GB to stay inside R2 10 GB free tier (default: 9.0)")
    parser.add_argument("--write-config", default="", help="Write public HTTPS base URL into assets/config.js")
    args = parser.parse_args()

    records, abs_map, skipped_priv = indexer.discover_source_files(include_private=False)
    total_bytes = sum(r["size"] for r in records)
    total_mb = total_bytes / (1024 * 1024)
    total_gb = total_bytes / (1024 * 1024 * 1024)
    print(f"Public courseware: {len(records)} files ({total_mb:.1f} MB / {total_gb:.2f} GB) | private excluded: {skipped_priv}")
    if total_gb > args.max_total_gb:
        print(f"ABORT: Total size {total_gb:.2f} GB exceeds safety cap {args.max_total_gb:.2f} GB (R2 free tier is 10 GB/month).", file=sys.stderr)
        sys.exit(3)

    if args.dry_run and not all(os.environ.get(v) for v in ("R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET")):
        print("[dry-run] R2_* env vars not set; local inventory check OK. Sample keys:")
        for r in records[:5]:
            print(f"  {args.prefix.strip('/')}/{r['id']}  ({r['size']} B, {guess_content_type(abs_map[r['id']])})")
        return

    missing = [v for v in ("R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET") if not os.environ.get(v)]
    if missing:
        print("ERROR: Missing required environment variables: " + ", ".join(missing), file=sys.stderr)
        print("See SETUP_R2.md for exact PowerShell setup commands.", file=sys.stderr)
        sys.exit(2)

    client = R2Client(
        os.environ["R2_ACCOUNT_ID"],
        os.environ["R2_ACCESS_KEY_ID"],
        os.environ["R2_SECRET_ACCESS_KEY"],
        os.environ["R2_BUCKET"],
    )
    prefix = args.prefix.strip("/")
    print(f"Checking existing objects in gs/r2 bucket '{client.bucket}' under '{prefix}/'...")
    remote_etags = client.list_etags(prefix + "/")
    print(f"Remote objects already present: {len(remote_etags)}")

    to_upload: list[tuple[str, Path, int]] = []
    skipped_same = 0
    for r in records:
        key = f"{prefix}/{r['id']}"
        path = abs_map[r["id"]]
        if key in remote_etags and remote_etags[key] == md5_hex(path):
            skipped_same += 1
            continue
        to_upload.append((key, path, r["size"]))

    upload_mb = sum(x[2] for x in to_upload) / (1024 * 1024)
    print(f"Plan: upload {len(to_upload)} files ({upload_mb:.1f} MB), skip {skipped_same} unchanged files.")
    if args.dry_run:
        for key, _, sz in to_upload[:15]:
            print(f"  [would upload] {key} ({sz} B)")
        return

    done = 0
    errors: list[str] = []
    with ThreadPoolExecutor(max_workers=max(1, min(args.workers, 12))) as pool:
        futs = {pool.submit(client.put_file, key, path): key for key, path, _ in to_upload}
        for fut in as_completed(futs):
            key = futs[fut]
            try:
                fut.result()
                done += 1
                if done % 25 == 0 or done == len(to_upload):
                    print(f"  uploaded {done}/{len(to_upload)} ...", flush=True)
            except Exception as exc:
                errors.append(f"{key}: {exc}")
                print(f"  FAIL {key}: {exc}", file=sys.stderr)

    if errors:
        print(f"Completed with {len(errors)} errors out of {len(to_upload)} files.", file=sys.stderr)
        sys.exit(1)

    print(f"Sync complete: {done} uploaded, {skipped_same} unchanged.")
    if args.write_config:
        update_config_js(args.write_config)


if __name__ == "__main__":
    main()
