import unittest
import sys
sys.path.append("../lib")
sys.path.append("../img")
import os.path
from os import path
from pillow_sample import PillowSample

class TestPillowSample(unittest.TestCase):
    def setUp(self):
        self.pillow_sample = PillowSample("../img/bird.jpg")

    def test_show_image(self):
        self.assertEqual((1200, 798), self.pillow_sample.image_size())

    def test_resize_image(self):
        self.assertEqual((1024, 768), self.pillow_sample.resize_image((1024, 768)))

    def test_save_image(self):
        self.pillow_sample.resize_image((1024, 768))
        self.pillow_sample.save_image("../img/bird_resize.jpg")
        self.assertEqual(True, path.exists("../img/bird_resize.jpg"))

if __name__ == "__main__":
    unittest.main()
