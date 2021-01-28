## 1. Environment

* Microsoft Windows 10 Home 10.0.19042 N/A Build 19042
* Python 3.9.1
  * pandas 1.2.1
  * Pillow 8.1.0
  * pip 21.0
  * selenium 3.141.0
  * urllib3 1.26.2

## 2. Reference

[PythonによるWebスクレイピング〜入門編〜【業務効率化への第一歩 - Udemy】

## 3. Clone the repository

```bash
$ git clone git@github.com:oasis-forever/web_scraping_tutorial.git
```

## 4. Web Driver

You need to have the following web driver before you execute web scraping.  

### 4-1. Windows

* For Google Chrome: [`./exec/chromedriver.exe`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/exec/chromedriver.exe)
* For Firefox: [`./exec/geckodriver.exe`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/exec/geckodriver.exe)

### 4-2. MacOS

* For Google Chrome
```bash
% brew install chromedriver
```

---

* For Firefox
```bash
% brew install geckodriver
```

### 4-3. Setup Checking

* For Google Chrome
```bash
% python ./lib/setup_chrome.py
```

\* In case of MaxOS, remove the argument of `webdriver.Chrome`.

```python
chrome = webdriver.Chrome()
```

---

* For Firefox
```bash
% python ./lib/setup_firefox.py
```

\* In case of MaxOS, remove the argument of `webdriver.Firefox`.

```python
chrome = webdriver.Firefox()
```

## 5. Sample Websites for Web Scraping

* [ログイン - Webスクレイピング入門](https://scraping-for-beginner.herokuapp.com/login_page)
* [講師情報 - Webスクレイピング入門](https://scraping-for-beginner.herokuapp.com/mypage)
* [ランキング - Webスクレイピング入門](https://scraping-for-beginner.herokuapp.com/ranking/)
* [画像 - Webスクレイピング入門](https://scraping-for-beginner.herokuapp.com/image)


## 6. Web Scraping

### 6-1. Simple DOM scraping

* Product Code: [`./lib/text_extractor.py`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/lib/text_extractor.py)
* Test Code: [`./test/test_text_extractor.py`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/test/test_text_extractor.py)
* CSV: [`./csv/lecturer_info.csv`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/csv/lecturer_info.csv)

### 6-2. More Complicated DOM scraping

* Product Code: [`./lib/info_collector.py`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/lib/info_collector.py)
  * Modules:
    * [`./lib/concerns/decimal_handler.py`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/lib/concerns/decimal_handler.py),
    * [`./lib/concerns/list_handler.py`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/lib/concerns/list_handler.py), 
* Test Code: [`./test/test_info_collector.py`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/test/test_info_collector.py)
* CSV: [`./csv/tour_reviews.csv`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/csv/tour_reviews.csv)

### 6-3. Pillow Sample

* Product Code: [`./lib/pillow_sample.py`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/lib/pillow_sample.py)
* Test Code: [`./test/test_pillow_sample.py`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/test/test_pillow_sample.py)
* Images:
  * [`./img/bird.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/bird.jpg)
  * [`./img/bird_resize.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/bird_resize.jpg)

### 6-4. Image Collector

* Product Code: [`./lib/image_collector.py`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/lib/image_collector.py)
* Test Code: [`./test/test_image_collector.py`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/test/test_image_collector.py)
* Images:
  * [`./img/image_01.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_01.jpg)
  * [`./img/image_02.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_02.jpg)
  * [`./img/image_03.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_03.jpg)
  * [`./img/image_04.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_04.jpg)
  * [`./img/image_05.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_05.jpg)
  * [`./img/image_06.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_06.jpg)
  * [`./img/image_07.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_07.jpg)
  * [`./img/image_08.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_08.jpg)
  * [`./img/image_09.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_09.jpg)
  * [`./img/image_10.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_10.jpg)
  * [`./img/image_11.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_11.jpg)
  * [`./img/image_12.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_12.jpg)
  * [`./img/image_13.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_13.jpg)
  * [`./img/image_14.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_14.jpg)
  * [`./img/image_15.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_15.jpg)
  * [`./img/image_16.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_16.jpg)
  * [`./img/image_17.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_17.jpg)
  * [`./img/image_18.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_18.jpg)
  * [`./img/image_19.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_19.jpg)
  * [`./img/image_20.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_20.jpg)
  * [`./img/image_21.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_21.jpg)
  * [`./img/image_22.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_22.jpg)
  * [`./img/image_23.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_23.jpg)
  * [`./img/image_24.jpg`](https://github.com/oasis-forever/web_scraping_tutorial/blob/master/img/image_24.jpg)
