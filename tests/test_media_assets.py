import tempfile
from pathlib import Path
import unittest
from media_assets import MediaAssets


class MediaTests(unittest.TestCase):
    def test_preview_dimensions_and_original_link_preserve_other_attributes(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);(root/'assets/optimized').mkdir(parents=True)
            (root/'assets/optimized/a.webp').write_bytes(b'preview')
            (root/'assets/a.png').write_bytes(b'original')
            manifest={'assets/a.png':{'preview':'assets/optimized/a.webp','width':800,'height':400}}
            output=MediaAssets(root,manifest).render('<img src="../../assets/a.png" alt="A &amp; B" class="diagram">','../../')
            self.assertIn('src="../../assets/optimized/a.webp"',output)
            self.assertIn('data-full-src="../../assets/a.png"',output)
            self.assertIn('width="800" height="400"',output)
            self.assertIn('alt="A &amp; B"',output)
            self.assertIn('loading="lazy"',output)
            self.assertEqual((root/'assets/a.png').read_bytes(),b'original')

    def test_missing_or_escaping_preview_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            for path in ['../outside.webp','assets/missing.webp']:
                with self.assertRaises(ValueError):
                    MediaAssets(Path(folder),{'assets/a.png':{'preview':path,'width':1,'height':1}})


if __name__=='__main__':unittest.main()
