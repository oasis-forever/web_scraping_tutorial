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
            i += 1
        self.assertEqual(True, path.exists("../img/image_01.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_02.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_03.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_04.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_05.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_06.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_07.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_08.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_09.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_10.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_11.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_12.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_13.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_14.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_15.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_16.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_17.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_18.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_19.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_20.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_21.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_22.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_23.jpg".format(i)))
        self.assertEqual(True, path.exists("../img/image_24.jpg".format(i)))

if __name__ == "__main__":
    unittest.main()
