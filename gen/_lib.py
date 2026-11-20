# -*- coding: utf-8 -*-
"""兼容层：老的 Course/lec API -> genlib.emit()。

有的脚本按 gen/_lib.py + Course(...).add(lec(...)).save() 写，
这里把它桥接到 study-site/genlib.py，统一写到 study-site/content/。
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_SITE = os.path.dirname(_HERE)
if _SITE not in sys.path:
    sys.path.insert(0, _SITE)

import genlib as _g

CONTENT_DIR = _g.CONTENT


def lec(slug, title_zh, title_en, keywords, source_files, html):
    return {
        "slug": slug,
        "title_zh": title_zh,
        "title_en": title_en,
        "keywords": list(keywords),
        "source_files": list(source_files),
        "html": html.strip(),
    }


class Course(object):
    def __init__(self, cid, order, name_zh, name_en, source_dir, summary=""):
        self.data = {
            "id": cid,
            "order": order,
            "name_zh": name_zh,
            "name_en": name_en,
            "source_dir": source_dir,
            "summary": summary,
            "lectures": [],
        }

    def add(self, *lectures):
        for item in lectures:
            self.data["lectures"].append(item)
        return self

    def save(self):
        _g.emit(
            self.data["id"], self.data["order"], self.data["name_zh"],
            self.data["name_en"], self.data["source_dir"], self.data["summary"],
            self.data["lectures"],
        )
        return os.path.join(CONTENT_DIR, self.data["id"] + ".json")
