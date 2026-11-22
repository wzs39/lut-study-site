#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scan original courseware folders, build bidirectional courseware index,
and optionally stage a clean <course_id>/<rel> tree for Google Cloud Storage sync.

Usage:
    python tools/build_courseware_index.py
    python tools/build_courseware_index.py --stage ../_gcs_stage --bucket lut-study-courseware
"""
from __future__ import annotations

import argparse
import glob
import json
import os
from pathlib import Path
import re
import shutil
import sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

SITE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SITE_ROOT.parent

# Course ID -> folder matching prefix (aligned with build.py CN2ID)
FOLDER_CODE_TO_ID = {
    "BH60A7201": "29911",
    "BH60A7400": "29913",
    "BM20A9200": "30565",
    "CT10A9900": "30331",
    "CT30A1000": "30332",
    "CT60A0250": "30352",
    "CT60A4050": "30361",
    "K200DJ96": "33295",
    "K200DJ99": "34583",
    "KE00BX35": "32667",
    "KE00DA03": "32632",
    "LUT digital orientation": "29428",
    "HDD4010": "62",
    "HDD4020": "80",
    "HDD5020": "86",
}

SKIP_NAMES = {".ds_store", "thumbs.db", "desktop.ini", "linked-manifest.json"}
SKIP_DIR_NAMES = {"_study_site", "__pycache__", ".git", "_info"}
PRIVATE_DIR_NAMES = {"submissions"}
PRIVATE_NAME_RE = re.compile(r"zishuo|004027128", re.I)
LOGIN_HTML_MARKERS = ("log in to the site", "forgotten your username", "shibboleth", "error 404")


def is_private_path(rel_posix: str) -> bool:
    parts = [p.lower() for p in rel_posix.split("/")]
    if any(p in PRIVATE_DIR_NAMES for p in parts):
        return True
    return bool(PRIVATE_NAME_RE.search(rel_posix))


def is_login_or_error_html(path: Path) -> bool:
    if path.suffix.lower() not in (".html", ".htm"):
        return False
    try:
        head = path.read_bytes()[:1200].decode("utf-8", errors="replace").lower()
    except OSError:
        return False
    return any(marker in head for marker in LOGIN_HTML_MARKERS)


def script_json(value) -> str:
    return (
        json.dumps(value, ensure_ascii=False, separators=(",", ":"))
        .replace("<", "\\u003c")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def resolve_course_id(folder_name: str) -> str | None:
    low = folder_name.lower()
    for code, cid in FOLDER_CODE_TO_ID.items():
        if code.lower() in low:
            return cid
    return None


def file_category(ext: str) -> str:
    ext = ext.lower()
    if ext == ".pdf":
        return "pdf"
    if ext in (".ppt", ".pptx", ".odp"):
        return "slides"
    if ext in (".doc", ".docx", ".odt", ".rtf", ".txt", ".md"):
        return "doc"
    if ext in (".mp3", ".wav", ".m4a", ".ogg", ".mp4", ".webm", ".mov"):
        return "media"
    if ext in (".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"):
        return "image"
    if ext in (".py", ".ipynb", ".c", ".cpp", ".java", ".js", ".ts", ".html", ".css", ".json", ".csv", ".xlsx", ".zip"):
        return "code"
    return "other"


def discover_source_files(include_private: bool = False) -> tuple[list[dict], dict[str, Path], int]:
    """Scan local source directories and return (records, id_to_abspath, skipped_private)."""
    source_roots = [REPO_ROOT / "学习资料", REPO_ROOT / "hebut" / "学习资料"]
    records: list[dict] = []
    abs_map: dict[str, Path] = {}
    seen_ids: set[str] = set()
    skipped_private = 0
    skipped_invalid_html = 0

    def add_file(cid: str, rel: str, path: Path) -> None:
        nonlocal skipped_private, skipped_invalid_html
        if path.name.lower() in SKIP_NAMES or path.name.startswith("~$"):
            return
        if not include_private and is_private_path(rel):
            skipped_private += 1
            return
        if is_login_or_error_html(path):
            skipped_invalid_html += 1
            return
        fid = f"{cid}/{rel}"
        if fid in seen_ids:
            return
        seen_ids.add(fid)
        ext = path.suffix.lower()
        records.append(
            {
                "id": fid,
                "cid": cid,
                "rel": rel,
                "name": path.name,
                "ext": ext,
                "cat": file_category(ext),
                "size": path.stat().st_size,
                "lectures": [],
            }
        )
        abs_map[fid] = path

    for root in source_roots:
        if not root.is_dir():
            continue
        for course_dir in sorted(root.iterdir()):
            if not course_dir.is_dir() or course_dir.name in SKIP_DIR_NAMES:
                continue
            cid = resolve_course_id(course_dir.name)
            if not cid:
                continue
            for path in sorted(course_dir.rglob("*")):
                if not path.is_file():
                    continue
                if any(part in SKIP_DIR_NAMES for part in path.parts):
                    continue
                rel = path.relative_to(course_dir).as_posix()
                add_file(cid, rel, path)

    # Also include supplemental linked PDFs archived under moodle-updates/*/linked/<cid>/
    updates_root = REPO_ROOT / "moodle-updates"
    if updates_root.is_dir():
        for linked_dir in sorted(updates_root.glob("*/linked/*")):
            if not linked_dir.is_dir():
                continue
            cid = linked_dir.name
            if not (SITE_ROOT / "content" / f"{cid}.json").is_file():
                continue
            for path in sorted(linked_dir.rglob("*")):
                if not path.is_file():
                    continue
                rel = "linked/" + path.relative_to(linked_dir).as_posix()
                add_file(cid, rel, path)

    if skipped_invalid_html:
        print(f"Filtered out {skipped_invalid_html} invalid Moodle login/error HTML snapshots")
    return records, abs_map, skipped_private


def _norm_key(text: str) -> str:
    s = text.replace("\\", "/").strip().lower()
    if s.endswith(".txt"):
        s = s[:-4]
    return re.sub(r"[\s_\-]+", "", s)


def _path_tokens(text: str) -> set[str]:
    s = text.replace("\\", "/").strip().lower()
    if s.endswith(".txt"):
        s = s[:-4]
    return set(re.findall(r"[a-z0-9äöå]{2,}", s))


def _pick_best_candidate(cand_str: str, candidates: list[dict]) -> dict | None:
    if len(candidates) == 1:
        return candidates[0]
    want = _path_tokens(cand_str)
    scored = []
    for r in candidates:
        have = _path_tokens(r["rel"])
        overlap = len(want & have)
        score = overlap / max(1, len(have))
        scored.append((overlap, score, r))
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    if scored and scored[0][0] >= 2:
        return scored[0][2]
    return None


def link_lectures(records: list[dict]) -> dict[str, list[dict]]:
    """Attach lecture references to courseware files and build lecture->files map."""
    by_cid: dict[str, list[dict]] = {}
    for rec in records:
        by_cid.setdefault(rec["cid"], []).append(rec)

    lecture_map: dict[str, list[str]] = {}
    matched_refs = 0
    total_refs = 0

    for cfile in sorted(glob.glob(str(SITE_ROOT / "content" / "*.json"))):
        course = json.loads(Path(cfile).read_text(encoding="utf-8"))
        cid = str(course["id"])
        pool = by_cid.get(cid, [])
        exact_rel = {r["rel"].lower(): r for r in pool}
        by_name: dict[str, list[dict]] = {}
        for r in pool:
            by_name.setdefault(r["name"].lower(), []).append(r)

        for lec in course.get("lectures", []):
            lid = f"{cid}/{lec['slug']}"
            lref = {"slug": lec["slug"], "title": lec.get("title_zh", lec["slug"])}
            linked_ids: list[str] = []

            for raw_sf in lec.get("source_files") or []:
                total_refs += 1
                sf = raw_sf.replace("\\", "/").strip()
                candidates = [sf]
                paren = re.findall(r"\(([^()]+\.[A-Za-z0-9]{1,5})\)", sf)
                candidates.extend(paren)
                hit: dict | None = None

                for cand in candidates:
                    low = cand.lower()
                    low_notxt = low[:-4] if low.endswith(".txt") else low
                    if low in exact_rel:
                        hit = exact_rel[low]
                    elif low_notxt in exact_rel:
                        hit = exact_rel[low_notxt]
                    else:
                        # First check flattened full-path match (e.g. 3_Assignments_2_..._intro_intro.html -> 3_Assignments/2_.../intro/intro.html)
                        nk_full = _norm_key(low_notxt)
                        for r in pool:
                            if _norm_key(r["rel"]) == nk_full:
                                hit = r
                                break
                        if not hit:
                            bn = Path(low).name
                            bn_notxt = Path(low_notxt).name
                            if bn in by_name:
                                hit = _pick_best_candidate(low_notxt, by_name[bn])
                            elif bn_notxt in by_name:
                                hit = _pick_best_candidate(low_notxt, by_name[bn_notxt])
                        if not hit:
                            bn_notxt = Path(low_notxt).name
                            nk = _norm_key(bn_notxt)
                            if len(nk) >= 6:
                                suffix_hits = [
                                    r for r in pool
                                    if len(_norm_key(r["name"])) >= 6
                                    and (nk.endswith(_norm_key(r["name"])) or _norm_key(r["name"]).endswith(nk))
                                ]
                                if suffix_hits:
                                    hit = _pick_best_candidate(low_notxt, suffix_hits)
                    if hit:
                        break

                if hit:
                    matched_refs += 1
                    if hit["id"] not in linked_ids:
                        linked_ids.append(hit["id"])
                    if not any(x["slug"] == lref["slug"] for x in hit["lectures"]):
                        hit["lectures"].append(lref)

            if linked_ids:
                lecture_map[lid] = linked_ids

    print(f"Courseware files indexed: {len(records)} | lecture source_files matched: {matched_refs}/{total_refs}")
    return lecture_map


def stage_for_gcs(abs_map: dict[str, Path], stage_dir: Path) -> int:
    """Create a clean <stage_dir>/<cid>/<rel> tree using hardlinks (falling back to copy)."""
    if stage_dir.exists():
        shutil.rmtree(stage_dir)
    stage_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for fid, src in abs_map.items():
        dst = stage_dir / fid
        dst.parent.mkdir(parents=True, exist_ok=True)
        try:
            os.link(src, dst)
        except OSError:
            shutil.copy2(src, dst)
        count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Build courseware index and optionally stage for cloud sync (R2 / GCS).")
    parser.add_argument("--stage", type=Path, default=None, help="Directory to stage <cid>/<rel> tree via hardlinks")
    parser.add_argument("--bucket", type=str, default="YOUR_BUCKET", help="Target bucket name for command hints")
    parser.add_argument("--include-private", action="store_true", help="Include personal Submissions/ and student-ID files (off by default)")
    args = parser.parse_args()

    records, abs_map, skipped_private = discover_source_files(include_private=args.include_private)
    lecture_map = link_lectures(records)
    if skipped_private:
        print(f"Privacy filter excluded {skipped_private} personal submission/CV files")

    total_bytes = sum(r["size"] for r in records)
    payload = {
        "version": 1,
        "totalFiles": len(records),
        "totalBytes": total_bytes,
        "files": records,
        "lectureFiles": lecture_map,
    }

    data_dir = SITE_ROOT / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "courseware-index.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    (data_dir / "courseware-index.js").write_text(
        "window.LUT_COURSEWARE_INDEX=" + script_json(payload) + ";\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Wrote data/courseware-index.json & .js ({len(records)} files, {total_bytes / (1024*1024):.1f} MB total)")

    if args.stage:
        staged = stage_for_gcs(abs_map, args.stage)
        print(f"Staged {staged} files into {args.stage.resolve()}")
        print(f"Next sync command:\n  gcloud storage rsync -r \"{args.stage.resolve()}\" gs://{args.bucket}/courseware")


if __name__ == "__main__":
    main()
