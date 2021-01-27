from selenium import webdriver

# Login
chrome = webdriver.Chrome(executable_path="../exec/chromedriver.exe")
chrome.get("https://scraping-for-beginner.herokuapp.com/login_page")
username = chrome.find_element_by_id("username")
username.send_keys("imanishi")
password = chrome.find_element_by_id("password")
password.send_keys("kohei")
login = chrome.find_element_by_id("login-btn")
login.click()

# Lecturer Info
ths = chrome.find_elements_by_tag_name("th")
keys = []
for th in ths:
    keys.append(th.text)

tds = chrome.find_elements_by_tag_name("td")
vals = []
for td in tds:
    if "\n" in td.text:
        vals.append(td.text.replace("\n", "、"))
    else:
        vals.append(td.text)

profile = {}
for i in range(len(keys)):
    profile[keys[i]] = vals[i]

print(profile)
# => {'講師名': '今西 航平', '所属企業': '株式会社キカガク', '生年月日': '1994年7月15日', '出身': '千葉県', '趣味': 'バスケットボール、読書、ガジェット集め'}
