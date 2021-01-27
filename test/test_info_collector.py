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

if __name__ == "__main__":
    unittest.main()
