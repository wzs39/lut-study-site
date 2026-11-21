"""Build offline search documents and the small learning catalogue."""
from html.parser import HTMLParser
import json
import hashlib
import re


SECTION_NAMES = {
    "overview":"本节定位与目标", "detail":"知识精讲", "keywords":"英文术语",
    "examples":"例题解析", "practice":"练习与解答", "exam":"考点与易错",
    "checklist":"方法清单", "mapping":"原始资料对照",
}


def script_json(value):
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":"))
            .replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))


class SearchSections(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.rows = []
        self.kind = None
        self.depth = 0
        self.anchor = ""
        self.title = ""
        self.parts = []
        self.heading = None
        self.heading_parts = []
        self.ignored = 0

    def flush(self):
        text = re.sub(r"\s+", " ", "".join(self.parts)).strip()
        if self.kind and text:
            self.rows.append({"kind":self.kind, "anchor":self.anchor, "title":self.title, "text":text})
        self.parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style"):
            self.ignored += 1
        if tag == "section":
            if not self.depth and attrs.get("data-type") in SECTION_NAMES:
                self.kind = attrs["data-type"]
                self.anchor = "sec-" + self.kind
                self.title = SECTION_NAMES[self.kind]
                self.depth = 1
            elif self.depth:
                self.depth += 1
        if not self.kind or self.ignored:
            return
        if tag in ("h2", "h3"):
            self.flush()
            self.heading = tag
            self.heading_parts = []
            self.anchor = attrs.get("id", self.anchor)
        if tag in ("p", "li", "br", "td", "th", "tr", "pre", "div", "h2", "h3"):
            self.parts.append(" ")
        if tag == "img" and attrs.get("alt"):
            self.parts.append(" " + attrs["alt"] + " ")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.ignored = max(0, self.ignored - 1)
        if tag == self.heading:
            self.title = re.sub(r"\s+", " ", "".join(self.heading_parts)).strip()
            self.heading = None
        if tag in ("p", "li", "td", "th", "tr", "div") and self.kind:
            self.parts.append(" ")
        if tag == "section" and self.depth:
            self.depth -= 1
            if not self.depth:
                self.flush()
                self.kind = None

    def handle_data(self, data):
        if self.kind and not self.ignored:
            self.parts.append(data)
            if self.heading:
                self.heading_parts.append(data)


def build_search_data(courses, decorate_body):
    documents, lectures, catalogue = [], [], []
    for course in courses:
        cid = str(course["id"])
        catalogue.append({"id":cid, "title":course.get("name_zh", cid)})
        for lecture in course.get("lectures", []):
            lecture_id = cid + "/" + lecture["slug"]
            url = "c/%s/%s.html" % (cid, lecture["slug"])
            common = {"lectureId":lecture_id, "course":cid,
                      "courseTitle":course.get("name_zh", cid), "lectureTitle":lecture.get("title_zh", ""),
                      "part":lecture.get("part", ""), "keywords":lecture.get("keywords", [])}
            parser = SearchSections()
            parser.feed(decorate_body(lecture.get("html", "")))
            parser.flush()
            for row in parser.rows:
                documents.append({**common, **row, "id":lecture_id + "/" + row["anchor"],
                                  "url":url + "#" + row["anchor"]})
            lectures.append({"id":lecture_id, "url":url, "course":cid,
                             "courseTitle":common["courseTitle"], "title":common["lectureTitle"],
                             "part":common["part"], "revision":hashlib.sha256(lecture.get("html", "").encode()).hexdigest()[:12]})
    return {"version":1, "courses":catalogue, "lectures":lectures, "documents":documents}
