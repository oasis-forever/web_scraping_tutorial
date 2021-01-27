import unittest
import sys
sys.path.append("../lib")
import os.path
from os import path
from web_scraper import WebScraper

class TestWebScraper(unittest.TestCase):
    def setUp(self):
        self.web_scraper = WebScraper("https://scraping-for-beginner.herokuapp.com/login_page")
        self.web_scraper.login("imanishi", "kohei")

    def test_get_lecturer_info(self):
        profile, *_ = self.web_scraper.get_lecturer_info()
        self.assertEqual({
            "講師名": "今西 航平",
            "所属企業": "株式会社キカガク",
            "生年月日": "1994年7月15日",
            "出身": "千葉県",
            "趣味": "バスケットボール、読書、ガジェット集め"
        }, profile)

    def test_export_csv(self):
        _, keys, vals = self.web_scraper.get_lecturer_info()
        self.web_scraper.export_csv(keys, vals, "../csv/lecturer_info.csv")
        self.assertEqual(True, path.exists("../csv/lecturer_info.csv"))

if __name__ == "__main__":
    unittest.main()
