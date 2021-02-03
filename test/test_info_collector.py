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
        titles = []
        evaluations = []
        rankings = []
        for i in range(1, 4):
            titles.append(self.info_collector.get_titles("?page={}".format(i)))
            evaluations.append(self.info_collector.get_evaluations("?page={}".format(i)))
            rankings.append(self.info_collector.get_rankings("?page={}".format(i)))
        self.titles = sum(titles, [])
        self.evaluations = sum(evaluations, [])
        self.rankings = sum(rankings, [])
        self.categories = self.info_collector.get_categories()

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
        ], self.titles)

    def test_get_evaluations(self):
        self.assertEqual([
            4.7, 4.7, 4.6, 4.5, 4.5, 4.4, 4.3, 4.3, 4.2, 4.1,
            4.1, 4.0, 3.9, 3.9, 3.8, 3.7, 3.7, 3.6, 3.5, 3.5,
            3.4, 3.3, 3.3, 3.2, 3.1, 3.1, 3.0, 2.9, 2.9, 2.8
        ], self.evaluations)

    def test_get_categories(self):
        self.categories = self.info_collector.get_categories()
        self.assertEqual(["楽しさ", "人混みの多さ", "景色", "アクセス"], self.categories)

    def test_get_rankings(self):
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
        ], self.rankings)

    # Comments are shown at random every time the browser is booted, so the value of each element cannot be tested.
    def test_get_comments(self):
        comments = []
        for i in range(1, 4):
            comments.append(self.info_collector.get_comments("?page={}".format(i)))
        self.assertEqual(30, len(sum(comments, [])))

    def test_export_csv(self):
        self.info_collector.export_csv(self.titles, self.evaluations, self.rankings, self.categories, "../csv/tour_reviews.csv")
        self.assertEqual(True, path.exists("../csv/tour_reviews.csv"))

if __name__ == "__main__":
    unittest.main()
