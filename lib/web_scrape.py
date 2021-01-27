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
