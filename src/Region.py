import operator
from Pixel import *

class Region:
    def __init__(self):
        self.pixels = []

    @property
    def size(self):
        return len(self.pixels)

    def add_pixel(self, pixel):
        self.pixels.append(pixel)

    def near_region(self, pixel):
        x = pixel.x
        y = pixel.y
        near_region = self.in_region(x + 1, y) or self.in_region(x - 1, y)
        near_region = near_region or self.in_region(x, y + 1) or self.in_region(x, y - 1)
        near_region = near_region or self.in_region(x + 1, y + 1) or self.in_region(x - 1, y - 1)
        near_region = near_region or self.in_region(x + 1, y - 1) or self.in_region(x - 1, y + 1)
        return near_region

    def in_region(self, x, y):
        for i in xrange(0, len(self.pixels)):
            pixel = self.pixels[i]
            if pixel.x == x and pixel.y == y:
                return True
        return False
    
    def number_of_skin_pixels(self):
        count = 0
        for i in xrange(0, len(self.pixels)):
            if self.pixels[i].is_skin():
                count += 1
        return count

    def average_intensity(self):
        intensities = [pixel.intensity() for pixel in self.pixels]
        return sum(intensities)/len(intensities)

    def topmost_pixel(self):
        self.pixels.sort(key = operator.attrgetter('x'), reverse=False)
        return self.pixels[0]

    def bottommost_pixel(self):
        self.pixels.sort(key = operator.attrgetter('x'), reverse=True)
        return self.pixels[0]

    def rightmost_pixel(self):
        self.pixels.sort(key = operator.attrgetter('y'), reverse=False)
        return self.pixels[0]

    def leftmost_pixel(self):
        self.pixels.sort(key = operator.attrgetter('y'), reverse=True)
        return self.pixels[0]
