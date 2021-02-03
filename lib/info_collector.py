from selenium import webdriver
import pandas as pd
import sys
sys.path.append("./concerns")
from list_handler import *

class InfoCollector:
    def __init__(self, base_url):
        self.chrome = webdriver.Chrome(executable_path="../exec/chromedriver.exe")
        self.base_url = base_url

    def _get_url(self, query_str=""):
        url = self.base_url + query_str
        self.chrome.get(url)

    def _get_ranking_items(self):
        elem_ranking_items = self.chrome.find_elements_by_class_name("u_categoryTipsItem")
        return elem_ranking_items

    def get_titles(self, query_str):
        self._get_url(query_str)
        elem_titles = self.chrome.find_elements_by_class_name("u_title")
        titles = []
        for elem_title in elem_titles:
            titles.append(elem_title.text.split("\n")[-1])
        return titles

    def get_evaluations(self, query_str):
        self._get_url(query_str)
        elem_rank_boxes = self.chrome.find_elements_by_class_name("u_rankBox")
        evaluations = []
        for elem_rank_box in elem_rank_boxes:
            evaluations.append(float(elem_rank_box.find_element_by_class_name("evaluateNumber").text))
        return evaluations

    def get_categories(self):
        self._get_url()
        elem_ranking_items = self._get_ranking_items()
        categories = tag_elems_list(elem_ranking_items, "dt")
        return categories[0]

    def get_rankings(self, query_str):
        self._get_url(query_str)
        elem_ranking_items = self._get_ranking_items()
        rankings = class_elems_list(elem_ranking_items, "is_rank")
        return rankings

    def get_comments(self, query_str):
        self._get_url(query_str)
        elem_ranking_items = self._get_ranking_items()
        comments = class_elems_list(elem_ranking_items, "comment")
        return comments

    def export_csv(self, titles, evaluations, rankings, categories, path):
        df = pd.DataFrame()
        df["観光地"] = titles
        df["総合評価"] = evaluations
        df_rankings = pd.DataFrame(rankings)
        df_rankings.columns = categories
        df = pd.concat([df, df_rankings], axis=1)
        df.to_csv(path)
