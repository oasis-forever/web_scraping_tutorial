from selenium import webdriver
import pandas as pd
import sys
sys.path.append("./concerns")
from list_handler import uniq_list

class InfoCollector:
    def __init__(self, url):
        self.chrome = webdriver.Chrome(executable_path="../exec/chromedriver.exe")
        self.chrome.get(url)

