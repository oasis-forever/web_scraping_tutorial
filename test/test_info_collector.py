import unittest
import sys
sys.path.append("../lib")
sys.path.append("../lib/concerns")
import os.path
from os import path
from info_collector import InfoCollector

class TestInfoCollector(unittest.TestCase):
    def setUp(self):
        self.info_collector = InfoCollector("https://scraping-for-beginner.herokuapp.com/ranking/")

    def test_get_titles(self):
        self.assertEqual([
            "観光地 1",
            "観光地 2",
            "観光地 3",
            "観光地 4",
            "観光地 5",
            "観光地 6",
            "観光地 7",
            "観光地 8",
            "観光地 9",
            "観光地 10",
        ], self.info_collector.get_titles())

    def test_get_evaluations(self):
        self.assertEqual([
            4.7,
            4.7,
            4.6,
            4.5,
            4.5,
            4.4,
            4.3,
            4.3,
            4.2,
            4.1
        ], self.info_collector.get_evaluations())

if __name__ == "__main__":
    unittest.main()
