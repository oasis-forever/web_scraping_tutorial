from selenium import webdriver
import pandas as pd
import sys
sys.path.append("./concerns")
from list_handler import uniq_list

class InfoCollector:
    def __init__(self, url):
        self.chrome = webdriver.Chrome(executable_path="../exec/chromedriver.exe")
        self.chrome.get(url)

    def get_titles(self):
        elem_titles = self.chrome.find_elements_by_class_name("u_title")
        titles = []
        for elem_title in elem_titles:
            titles.append(elem_title.text.split("\n")[-1])
        return titles

