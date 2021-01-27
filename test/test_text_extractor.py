import unittest
import sys
sys.path.append("../lib")
import os.path
from os import path
from text_extractor import TextExtractor

class TestTextExtractor(unittest.TestCase):
    def setUp(self):
        self.text_extractor = TextExtractor("https://scraping-for-beginner.herokuapp.com/login_page")
        self.text_extractor.login("imanishi", "kohei")

    def test_get_lecturer_info(self):
        profile, *_ = self.text_extractor.get_lecturer_info()
        self.assertEqual({
            "講師名": "今西 航平",
            "所属企業": "株式会社キカガク",
            "生年月日": "1994年7月15日",
            "出身": "千葉県",
            "趣味": "バスケットボール、読書、ガジェット集め"
        }, profile)

    def test_export_csv(self):
        _, keys, vals = self.text_extractor.get_lecturer_info()
        self.text_extractor.export_csv(keys, vals, "../csv/lecturer_info.csv")
        self.assertEqual(True, path.exists("../csv/lecturer_info.csv"))

if __name__ == "__main__":
    unittest.main()
