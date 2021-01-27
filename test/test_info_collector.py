import unittest
import sys
sys.path.append("../lib")
import os.path
from os import path
from info_collector import InfoCollector

class TestInfoCollector(unittest.TestCase):
    def test_get_titles(self):
        titles = []
        for i in range(1, 4):
            info_collector = InfoCollector("https://scraping-for-beginner.herokuapp.com/ranking/?page={}".format(i))
            titles.append(info_collector.get_titles())
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
            "観光地 11",
            "観光地 12",
            "観光地 13",
            "観光地 14",
            "観光地 15",
            "観光地 16",
            "観光地 17",
            "観光地 18",
            "観光地 19",
            "観光地 20",
            "観光地 21",
            "観光地 22",
            "観光地 23",
            "観光地 24",
            "観光地 25",
            "観光地 26",
            "観光地 27",
            "観光地 28",
            "観光地 29",
            "観光地 30",
        ], sum(titles, []))

    def test_get_evaluations(self):
        evaluations = []
        for i in range(1, 4):
            info_collector = InfoCollector("https://scraping-for-beginner.herokuapp.com/ranking/?page={}".format(i))
            evaluations.append(info_collector.get_evaluations())
        self.assertEqual([
            4.7, 4.7, 4.6, 4.5, 4.5, 4.4, 4.3, 4.3, 4.2, 4.1,
            4.1, 4.0, 3.9, 3.9, 3.8, 3.7, 3.7, 3.6, 3.5, 3.5,
            3.4, 3.3, 3.3, 3.2, 3.1, 3.1, 3.0, 2.9, 2.9, 2.8
        ], sum(evaluations, []))

    def test_get_categories(self):
        info_collector = InfoCollector("https://scraping-for-beginner.herokuapp.com/ranking/")
        self.assertEqual(["楽しさ", "人混みの多さ", "景色", "アクセス"], info_collector.get_categories())

    def test_get_rankings(self):
        rankings = []
        for i in range(1, 4):
            info_collector = InfoCollector("https://scraping-for-beginner.herokuapp.com/ranking/?page={}".format(i))
            rankings.append(info_collector.get_rankings())
        self.assertEqual([
            [4.6, 4.5, 4.9, 4.2],
            [4.6, 4.5, 4.9, 4.2],
            [4.5, 4.4, 4.8, 4.1],
            [4.4, 4.4, 4.8, 4.0],
            [4.4, 4.3, 4.7, 4.0],
            [4.3, 4.3, 4.7, 3.9],
            [4.2, 4.2, 4.6, 3.8],
            [4.2, 4.2, 4.6, 3.8],
            [4.1, 4.1, 4.5, 3.7],
            [4.0, 4.1, 4.4, 3.6],
            [4.0, 4.0, 4.4, 3.6],
            [3.9, 4.0, 4.3, 3.5],
            [3.8, 3.9, 4.3, 3.4],
            [3.8, 3.9, 4.2, 3.4],
            [3.7, 3.8, 4.2, 3.3],
            [3.6, 3.8, 4.1, 3.2],
            [3.6, 3.7, 4.1, 3.2],
            [3.5, 3.7, 4.0, 3.1],
            [3.4, 3.6, 3.9, 3.0],
            [3.4, 3.6, 3.9, 3.0],
            [3.3, 3.5, 3.8, 2.9],
            [3.2, 3.5, 3.8, 2.8],
            [3.2, 3.4, 3.7, 2.8],
            [3.1, 3.4, 3.7, 2.7],
            [3.0, 3.3, 3.6, 2.6],
            [3.0, 3.3, 3.6, 2.6],
            [2.9, 3.2, 3.5, 2.5],
            [2.8, 3.2, 3.4, 2.4],
            [2.8, 3.1, 3.4, 2.4],
            [2.7, 3.1, 3.3, 2.3]
        ], sum(rankings, []))

    # Comments are shown at random every time the browser is booted, so the value of each element cannot be tested.
    def test_get_comments(self):
        comments = []
        for i in range(1, 4):
            info_collector = InfoCollector("https://scraping-for-beginner.herokuapp.com/ranking/?page={}".format(i))
            comments.append(info_collector.get_comments())
        self.assertEqual(30, len(sum(comments, [])))

    def test_export_csv(self):
        tmp_titles = []
        tmp_evaluations = []
        tmp_rankings = []
        for i in range(1, 4):
            info_collector = InfoCollector("https://scraping-for-beginner.herokuapp.com/ranking/?page={}".format(i))
            tmp_titles.append(info_collector.get_titles())
            tmp_evaluations.append(info_collector.get_evaluations())
            tmp_rankings.append(info_collector.get_rankings())
        titles = sum(tmp_titles, [])
        evaluations = sum(tmp_evaluations, [])
        rankings = sum(tmp_rankings, [])
        info_collector = InfoCollector("https://scraping-for-beginner.herokuapp.com/ranking/")
        categories = info_collector.get_categories()
        info_collector.export_csv(titles, evaluations, categories, rankings, "../csv/tour_reviews.csv")
        self.assertEqual(True, path.exists("../csv/tour_reviews.csv"))

if __name__ == "__main__":
    unittest.main()
