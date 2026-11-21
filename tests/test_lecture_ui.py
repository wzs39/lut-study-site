"""Regression checks for the generated lecture reading interface."""
import importlib.util
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("site_builder", ROOT / "build.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class Elements(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.nodes = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.nodes.append((tag, dict(attrs)))

    def select(self, tag, **attrs):
        return [a for t, a in self.nodes if t == tag
                and all(a.get(k.replace("_", "-")) == v for k, v in attrs.items())]


class LectureInterfaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.courses = builder.load_courses()

    def test_every_lecture_has_accessible_navigation_and_intact_content(self):
        for course in self.courses:
            for index, lecture in enumerate(course["lectures"]):
                with self.subTest(course=course["id"], lecture=lecture["slug"]):
                    page = builder.build_lecture(course, index)
                    dom = Elements(page)
                    self.assertEqual(len(dom.select("h1", id="lecture-title")), 1)
                    self.assertEqual(len(dom.select("main", id="main-content")), 1)
                    self.assertTrue(dom.select("a", href="#page-content"))
                    self.assertEqual(len(dom.select("aside", **{"class": "page-side"})), 1)
                    self.assertTrue(dom.select("button", id="directory-toggle", aria_controls="directory-content"))
                    self.assertTrue(dom.select("nav", aria_label="本页目录"))
                    local = re.search(r'<nav\b[^>]*aria-label="本页目录"[^>]*>.*?</nav>', page, flags=re.S)
                    links = Elements(local.group(0)).select("a")
                    for kind in builder.REQUIRED:
                        self.assertTrue(any(a.get("href") == "#sec-" + kind for a in links))
                    current = dom.select("a", aria_current="page")
                    self.assertEqual(len(current), 1)
                    self.assertEqual(current[0]["href"], lecture["slug"] + ".html")
                    for kind in builder.REQUIRED:
                        self.assertTrue(dom.select("section", data_type=kind))
                    # All source content survives; only table scroll regions are added.
                    expected, _ = builder.decorate(builder.add_section_ids(
                        builder.fix_assets(lecture["html"], "../../")))
                    expected = builder.MEDIA.render(expected, '../../')
                    expected = builder.encode_inline_controls(expected)
                    expected_dom = Elements(expected)
                    unwrapped = re.sub(
                        '<div class="table-scroll" role="region" tabindex="0" '
                        r'aria-label="讲义表格 \d+，可横向滚动">', "", page
                    ).replace("</table></div>", "</table>")
                    self.assertIn(expected, unwrapped)
                    self.assertEqual(len(dom.select("table")), len(expected_dom.select("table")))
                    self.assertEqual(len(dom.select("div", role="region", tabindex="0")),
                                     len(expected_dom.select("table")))
                    labels = [a["aria-label"] for a in dom.select("div", role="region", tabindex="0")]
                    self.assertEqual(len(labels), len(set(labels)))
                    self.assertEqual(Elements(page).select("img"), expected_dom.select("img"))

    def test_all_sidebar_and_section_fragment_links_resolve(self):
        for course in self.courses:
            for index in range(len(course["lectures"])):
                dom = Elements(builder.build_lecture(course, index))
                ids = {a["id"] for _, a in dom.nodes if "id" in a}
                for _, attrs in dom.nodes:
                    href = attrs.get("href", "")
                    if href.startswith("#") and len(href) > 1:
                        self.assertIn(href[1:], ids)

    def test_lecture_text_and_source_metadata_remain_escaped(self):
        course = {"id": "test", "name_zh": "A & B", "lectures": [
            {"slug": "one", "title_zh": '<script>alert("title")</script>',
             "title_en": "A < B", "part": "P & Q", "source_files": ["<source>.pdf"],
             "html": '<section class="card" data-type="overview"><h2>Intro</h2></section>'}
        ]}
        page = builder.build_lecture(course, 0)
        self.assertNotIn('<script>alert("title")</script>', page)
        self.assertIn("&lt;source&gt;.pdf", page)
        self.assertIn("A &lt; B", page)

    def test_inline_control_characters_keep_their_text_without_raw_carriage_returns(self):
        body='<p>CR: <code>\r</code>; LF: <code>\n</code>; CRLF: <code>\r\n</code></p><pre><code>line one\nline two</code></pre>'
        encoded=builder.encode_inline_controls(body)
        self.assertIn('<code>&#13;</code>',encoded)
        self.assertIn('<code>&#10;</code>',encoded)
        self.assertIn('<code>&#13;&#10;</code>',encoded)
        self.assertIn('line one\nline two',encoded)
        self.assertEqual(__import__('html').unescape(encoded),body)


if __name__ == "__main__":
    unittest.main()
