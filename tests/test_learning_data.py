import unittest

from test_lecture_ui import builder
from learning_data import build_search_data, script_json


class SearchDataTests(unittest.TestCase):
    def test_all_lectures_and_body_sections_are_searchable(self):
        courses = builder.load_courses()
        data = build_search_data(courses, lambda body: builder.decorate(builder.add_section_ids(body))[0])
        self.assertEqual(len(data["lectures"]), 133)
        self.assertGreaterEqual(len(data["documents"]), 133 * 8)
        ids = [doc["id"] for doc in data["documents"]]
        self.assertEqual(len(ids), len(set(ids)))
        for doc in data["documents"]:
            self.assertIn("#", doc["url"])
            self.assertTrue(doc["text"].strip())

    def test_heading_id_and_hidden_answer_text_are_retained(self):
        courses = [{"id":"c1","name_zh":"测试课","lectures":[{
            "slug":"one","title_zh":"第一讲","keywords":["matrix"],"html":
            '<section data-type="detail"><h2 id="real-id">子节</h2><p>仅正文存在的短语</p>'
            '<details><summary>答案</summary><p>隐藏答案也可搜索</p></details></section>'
        }]}]
        data = build_search_data(courses, lambda body: body)
        doc = next(d for d in data["documents"] if "仅正文" in d["text"])
        self.assertEqual(doc["url"], "c/c1/one.html#real-id")
        self.assertIn("隐藏答案也可搜索", doc["text"])
        self.assertEqual(data["lectures"][0]["id"], "c1/one")

    def test_script_data_cannot_close_its_script_element(self):
        value = script_json({"text":"</script><img onerror=alert(1)>\u2028"})
        self.assertNotIn("</script>", value)
        import json
        self.assertEqual(json.loads(value)["text"], "</script><img onerror=alert(1)>\u2028")


if __name__ == "__main__":
    unittest.main()
