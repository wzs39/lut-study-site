"""Unit tests for courseware privacy filtering and Cloudflare R2 SigV4 sync utilities."""
import datetime
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import build_courseware_index as indexer  # noqa: E402
import sync_r2  # noqa: E402


class CoursewareAndR2Tests(unittest.TestCase):
    def test_privacy_filter_excludes_submissions_and_student_id_but_keeps_instructions(self):
        self.assertTrue(indexer.is_private_path("5_Assignments/2_Upload your CV/Submissions/Zishuo Wang/Zishuo_Wang_CV.pdf"))
        self.assertTrue(indexer.is_private_path("Week2- Number systems/Zishuo Wang 004027128_Exercise1.pdf"))
        self.assertTrue(indexer.is_private_path("20_Course Project/1_Proposal/Submissions/Group 1/Proposal.pdf"))
        self.assertFalse(indexer.is_private_path("2_Climate.now Essay Task Instructions and Submission Tool/intro/Climate.now_Essay Task.pdf"))
        self.assertFalse(indexer.is_private_path("Chapter 1/1_Lecture1.pdf"))

    def test_sigv4_headers_format_and_uri_encoding(self):
        fixed_now = datetime.datetime(2026, 11, 22, 12, 0, 0, tzinfo=datetime.timezone.utc)
        headers = sync_r2.sign_v4_headers(
            method="PUT",
            host="abc123.r2.cloudflarestorage.com",
            canonical_uri="/my-bucket/courseware/33295/Tunti%201%20%C3%A4.pdf",
            query_params={},
            extra_headers={"Content-Type": "application/pdf"},
            payload_sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            access_key="AKIA_TEST",
            secret_key="SECRET_TEST",
            now=fixed_now,
        )
        self.assertEqual(headers["x-amz-date"], "20261122T120000Z")
        self.assertIn("AWS4-HMAC-SHA256 Credential=AKIA_TEST/20261122/auto/s3/aws4_request", headers["authorization"])
        self.assertIn("SignedHeaders=content-type;host;x-amz-content-sha256;x-amz-date", headers["authorization"])
        self.assertEqual(sync_r2.aws_encode("Tunti 1 ä.pdf"), "Tunti%201%20%C3%A4.pdf")

    def test_mime_types_for_courseware_formats(self):
        self.assertEqual(sync_r2.guess_content_type(Path("lec.pdf")), "application/pdf")
        self.assertIn("presentationml", sync_r2.guess_content_type(Path("slides.pptx")))
        self.assertIn("wordprocessingml", sync_r2.guess_content_type(Path("notes.docx")))
        self.assertEqual(sync_r2.guess_content_type(Path("audio.mp3")), "audio/mpeg")


if __name__ == "__main__":
    unittest.main()
