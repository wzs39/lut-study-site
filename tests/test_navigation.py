"""The navigation contract is shared by every generated module/page type."""
import re
import posixpath
import unittest
from urllib.parse import unquote, urlsplit

from test_lecture_ui import builder, Elements


def nav_nodes(page, label):
    match = re.search(r'<nav\b[^>]*aria-label="%s"[^>]*>.*?</nav>' % label,
                      page, flags=re.S)
    return Elements(match.group(0)).nodes if match else []


class UnifiedNavigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.courses = builder.load_courses()
        cls.pages = [
            ("index.html", "courses", builder.build_root(cls.courses)),
            ("review.html", "review", builder.build_review(cls.courses)),
            ("extend.html", "extension", builder.build_extension(cls.courses)),
            ("all.html", "reader", builder.build_allinone(cls.courses)),
            ("upload.html", "upload", builder.build_upload(cls.courses)),
        ]
        for course in cls.courses:
            prefix = "c/%s/" % course["id"]
            cls.pages.append((prefix + "index.html", "courses", builder.build_course(course)))
            cls.pages.append((prefix + "reader.html", "reader", builder.build_allinone([course], "../../")))
            cls.pages.extend((prefix + builder.part_slug(i) + ".html", "courses",
                              builder.build_part(course, i))
                             for i in range(len(builder.parts_of(course))))
            cls.pages.extend((prefix + lec["slug"] + ".html", "courses",
                              builder.build_lecture(course, i))
                             for i, lec in enumerate(course["lectures"]))

    def test_every_module_uses_one_directory_and_the_same_five_module_links(self):
        signature = None
        for path, module, page in self.pages:
            with self.subTest(page=path):
                dom = Elements(page)
                self.assertEqual(len(dom.select("aside", **{"class": "page-side"})), 1)
                self.assertEqual(len(dom.select("button", id="directory-toggle")), 1)
                self.assertEqual(len(dom.select("nav", aria_label="本页目录")), 1)
                self.assertEqual(len(dom.select("div", id="page-content")), 1)
                self.assertTrue(dom.select("a", href="#page-content"))
                self.assertTrue(dom.select("body", data_module=module))
                links = [a for t, a in nav_nodes(page, "站点导航") if t == "a"]
                self.assertEqual(len(links), 5)
                current = [a for a in links if a.get("aria-current") in ("page", "true")]
                self.assertEqual(len(current), 1)
                self.assertEqual(current[0]["data-module-link"], module)
                actual = [(a["data-module-link"], a["href"].split("/")[-1]) for a in links]
                if signature is None:
                    signature = actual
                self.assertEqual(actual, signature)
                self.assertNotIn('class="snavs"', page)
                self.assertNotIn('class="alltoc"', page)

    def test_breadcrumb_and_directory_destinations_resolve_on_all_pages(self):
        available = {path for path, _, _ in self.pages}
        for path, _, page in self.pages:
            with self.subTest(page=path):
                dom = Elements(page)
                ids = {a["id"] for _, a in dom.nodes if "id" in a}
                trail = nav_nodes(page, "当前位置")
                self.assertTrue(any(t == "ol" for t, _ in trail))
                self.assertEqual(sum(a.get("aria-current") == "page" for _, a in trail), 1)
                for label in ["站点导航", "当前位置", "本页目录", "课程目录", "顺序导航"]:
                    for tag, attrs in nav_nodes(page, label):
                        if tag != "a":
                            continue
                        href = attrs.get("href", "")
                        url = urlsplit(href)
                        if not url.path:
                            self.assertIn(unquote(url.fragment), ids, (path, href))
                        else:
                            target = posixpath.normpath(posixpath.join(posixpath.dirname(path), url.path))
                            self.assertIn(target, available, (path, href))
                for attrs in dom.select("button"):
                    if "aria-controls" in attrs:
                        self.assertIn(attrs["aria-controls"], ids)

    def test_course_hierarchy_is_identical_from_course_chapter_and_lecture(self):
        for course in self.courses:
            pages = [builder.build_course(course), builder.build_part(course, 0),
                     builder.build_lecture(course, 0)]
            destinations = [[a["href"] for t, a in nav_nodes(page, "课程目录") if t == "a"]
                            for page in pages]
            self.assertTrue(destinations[0])
            self.assertEqual(destinations[0], destinations[1])
            self.assertEqual(destinations[1], destinations[2])
            self.assertEqual(sum(a.get("aria-current") == "page"
                                 for t, a in nav_nodes(pages[2], "课程目录") if t == "a"), 1)

    def test_chapter_and_lecture_share_previous_parent_next_navigation(self):
        for course in self.courses:
            for page in [builder.build_part(course, 0), builder.build_lecture(course, 0)]:
                nodes = nav_nodes(page, "顺序导航")
                self.assertTrue(nodes)
                self.assertTrue(any(t == "a" and a.get("data-sequence") == "parent" for t, a in nodes))
                self.assertEqual(sum(a.get("data-sequence") == "previous" for _, a in nodes), 1)
                self.assertEqual(sum(a.get("data-sequence") == "next" for _, a in nodes), 1)


if __name__ == "__main__":
    unittest.main()
