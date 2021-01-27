from selenium import webdriver
import io
from urllib import request
from PIL import Image
import sys
sys.path.append("../img")

class ImageCollector:
    def __init__(self, url):
        self.chrome = webdriver.Chrome(executable_path="../exec/chromedriver.exe")
        self.chrome.get(url)

    def get_images(self):
        img_divs = self.chrome.find_elements_by_class_name("material-placeholder")
        img_urls = []
        for img_div in img_divs:
            img_urls.append(img_div.find_element_by_tag_name("img").get_attribute("src"))
        images = []
        for img_url in img_urls:
            f = io.BytesIO(request.urlopen(img_url).read())
            image = Image.open(f)
            images.append(image)
        return images

    def save_image(self, image, path):
        image.save(path)
