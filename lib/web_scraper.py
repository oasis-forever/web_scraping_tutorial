from selenium import webdriver

class WebScraper:
    def __init__(self, url):
        self.chrome = webdriver.Chrome(executable_path="../exec/chromedriver.exe")
        self.chrome.get(url)

    def login(self, user_name, pwd):
        username = self.chrome.find_element_by_id("username")
        username.send_keys(user_name)
        password = self.chrome.find_element_by_id("password")
        password.send_keys(pwd)
        login = self.chrome.find_element_by_id("login-btn")
        login.click()

    def get_lecturer_info(self):
        ths = self.chrome.find_elements_by_tag_name("th")
        keys = []
        for th in ths:
            keys.append(th.text)
        tds = self.chrome.find_elements_by_tag_name("td")
        vals = []
        for td in tds:
            if "\n" in td.text:
                vals.append(td.text.replace("\n", "、"))
            else:
                vals.append(td.text)
        profile = {}
        for i in range(len(keys)):
            profile[keys[i]] = vals[i]
        return profile
