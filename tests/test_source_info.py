import json
from pathlib import Path
import tempfile
import unittest

from source_info import SourceCatalogue, source_panel


class ProvenanceTests(unittest.TestCase):
    def test_missing_metadata_does_not_invent_review_dates_or_files(self):
        with tempfile.TemporaryDirectory() as folder:
            sources=SourceCatalogue(Path(folder))
            lecture={"slug":"one","source_files":["original.pdf"],"html":"content"}
            panel=source_panel({"id":"1"},lecture,sources)
            self.assertIn("未记录",panel)
            self.assertIn("未附原文件",panel)
            self.assertNotIn('href="original.pdf"',panel)
            self.assertNotIn("生成于",panel)

    def test_actual_pdf_and_registered_page_link(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);(root/'sources/1').mkdir(parents=True)
            (root/'sources/1/original.pdf').write_bytes(b'%PDF-1.4 test')
            (root/'data').mkdir()
            metadata={"version":1,"lectures":{"1/one":{"reviewed_at":"2020-01-02","source_version":"2020 edition",
                       "sources":[{"name":"original.pdf","path":"sources/1/original.pdf","page":3}]}}}
            (root/'data/source-metadata.json').write_text(json.dumps(metadata),encoding='utf-8')
            panel=source_panel({"id":"1"},{"slug":"one","source_files":["original.pdf"],"html":"content"},SourceCatalogue(root),prefix='../../')
            self.assertIn('../../sources/1/original.pdf#page=3',panel)
            self.assertIn('2020-01-02',panel);self.assertIn('2020 edition',panel)

    def test_rejects_traversal_script_urls_missing_paths_and_fake_dates(self):
        for source,metadata in [
            ({"name":"x.pdf","path":"../outside.pdf"},{}),
            ({"name":"x.pdf","url":"javascript:alert(1)"},{}),
            ({"name":"x.pdf","path":"sources/missing.pdf"},{}),
            ({"name":"x.pdf"},{"reviewed_at":"2999-01-01"}),
        ]:
            with self.subTest(source=source,metadata=metadata),tempfile.TemporaryDirectory() as folder:
                root=Path(folder);(root/'data').mkdir()
                (root/'data/source-metadata.json').write_text(json.dumps({"version":1,"lectures":{"1/one":{**metadata,"sources":[source]}}}),encoding='utf-8')
                with self.assertRaises(ValueError):
                    source_panel({"id":"1"},{"slug":"one","source_files":["x.pdf"],"html":""},SourceCatalogue(root))


if __name__=='__main__':
    unittest.main()
