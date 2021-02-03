import unittest
import sys
sys.path.append("../lib")
sys.path.append("../img")
import os.path
from os import path
from image_collector import ImageCollector

class TestImageCollector(unittest.TestCase):
    def setUp(self):
        self.image_collector = ImageCollector("https://scraping-for-beginner.herokuapp.com/image")

    def test_get_images(self):
        self.assertEqual(24, len(self.image_collector.get_images()))

    def test_save_images(self):
        self.image_collector.get_images()
        self.image_collector.save_images("../img/image_{:0=2}.jpg")
        self.assertEqual(True, path.exists("../img/image_01.jpg"))
        self.assertEqual(True, path.exists("../img/image_02.jpg"))
        self.assertEqual(True, path.exists("../img/image_03.jpg"))
        self.assertEqual(True, path.exists("../img/image_04.jpg"))
        self.assertEqual(True, path.exists("../img/image_05.jpg"))
        self.assertEqual(True, path.exists("../img/image_06.jpg"))
        self.assertEqual(True, path.exists("../img/image_07.jpg"))
        self.assertEqual(True, path.exists("../img/image_08.jpg"))
        self.assertEqual(True, path.exists("../img/image_09.jpg"))
        self.assertEqual(True, path.exists("../img/image_10.jpg"))
        self.assertEqual(True, path.exists("../img/image_11.jpg"))
        self.assertEqual(True, path.exists("../img/image_12.jpg"))
        self.assertEqual(True, path.exists("../img/image_13.jpg"))
        self.assertEqual(True, path.exists("../img/image_14.jpg"))
        self.assertEqual(True, path.exists("../img/image_15.jpg"))
        self.assertEqual(True, path.exists("../img/image_16.jpg"))
        self.assertEqual(True, path.exists("../img/image_17.jpg"))
        self.assertEqual(True, path.exists("../img/image_18.jpg"))
        self.assertEqual(True, path.exists("../img/image_19.jpg"))
        self.assertEqual(True, path.exists("../img/image_20.jpg"))
        self.assertEqual(True, path.exists("../img/image_21.jpg"))
        self.assertEqual(True, path.exists("../img/image_22.jpg"))
        self.assertEqual(True, path.exists("../img/image_23.jpg"))
        self.assertEqual(True, path.exists("../img/image_24.jpg"))

if __name__ == "__main__":
    unittest.main()
