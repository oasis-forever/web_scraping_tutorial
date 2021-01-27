from selenium import webdriver
import pandas as pd
import sys

class InfoCollector:
    def __init__(self, url):
        self.chrome = webdriver.Chrome(executable_path="../exec/chromedriver.exe")
        self.chrome.get(url)

    def _get_ranking_items(self):
        elem_ranking_items = self.chrome.find_elements_by_class_name("u_categoryTipsItem")
        return elem_ranking_items

    def get_titles(self):
        elem_titles = self.chrome.find_elements_by_class_name("u_title")
        titles = []
        for elem_title in elem_titles:
            titles.append(elem_title.text.split("\n")[-1])
        return titles

    def get_evaluations(self):
        elem_rank_boxes = self.chrome.find_elements_by_class_name("u_rankBox")
        evaluations = []
        for elem_rank_box in elem_rank_boxes:
            evaluations.append(float(elem_rank_box.find_element_by_class_name("evaluateNumber").text))
        return evaluations

    def get_categories(self):
        elem_ranking_items = self._get_ranking_items()
        categories = []
        for elem_ranking_item in elem_ranking_items:
            _categories = []
            for dt in elem_ranking_item.find_elements_by_tag_name("dt"):
                _categories.append(dt.text)
            categories.append(_categories)
        return categories[0]

    def get_rankings(self):
        elem_ranking_items = self._get_ranking_items()
        rankings = []
        for elem_ranking_item in elem_ranking_items:
            _rankings = []
            for ranking in elem_ranking_item.find_elements_by_class_name("is_rank"):
                _rankings.append(float(ranking.text))
            rankings.append(_rankings)
        return rankings

    def get_comments(self):
        elem_ranking_items = self._get_ranking_items()
        comments = []
        for elem_ranking_item in elem_ranking_items:
            _comments = []
            for comment in elem_ranking_item.find_elements_by_class_name("comment"):
                _comments.append(comment.text)
            comments.append(_comments)
        return comments

    def export_csv(self, titles, evaluations, categories, rankings, path):
        df = pd.DataFrame()
        df["観光地"] = titles
        df["総合評価"] = evaluations
        df_rankings = pd.DataFrame(rankings)
        df_rankings.columns = categories
        df = pd.concat([df, df_rankings], axis=1)
        df.to_csv(path)
