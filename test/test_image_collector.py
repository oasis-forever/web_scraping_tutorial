import unittest
import sys
sys.path.append("../lib")
sys.path.append("../img")
import os.path
from os import path
from image_collector import ImageCollector

class TestTextExtractor(unittest.TestCase):
    def setUp(self):
        self.image_collector = ImageCollector("https://scraping-for-beginner.herokuapp.com/image")

    def test_get_images(self):
        self.assertEqual(24, len(self.image_collector.get_images()))

    def test_save_images(self):
        images = self.image_collector.get_images()
        i = 1
        for image in images:
            self.image_collector.save_image(image, "../img/image_{:0=2}.jpg".format(i))
            self.assertEqual(True, path.exists("../img/image_{:0=2}.jpg".format(i)))
            i += 1

if __name__ == "__main__":
    unittest.main()
