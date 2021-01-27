from PIL import Image
import sys
sys.path.append("../img")

class PillowSample:
    def __init__(self, path):
        self.image = Image.open(path)

    def image_size(self):
        return self.image.size

    def resize_image(self, size):
        return self.image.resize(size).size

    def save_image(self, path):
        self.image.save(path)
