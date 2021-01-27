from selenium import webdriver
import pandas as pd
import sys
sys.path.append("./concerns")
from list_handler import uniq_list

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

