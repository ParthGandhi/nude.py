import operator
from Pixel import *

class Region:
    def __init__(self):
        self.pixels = []
        self.size = 0

    def get_size(self):
        return self.size

    def add_pixel(self, pixel):
        self.size += 1
        self.pixels.append(pixel)

    def near_region(self, pixel):
        x = pixel.get_x()
        y = pixel.get_y()
        near_region = self.in_region(x + 1, y) or self.in_region(x - 1, y)
        near_region = near_region or self.in_region(x, y + 1) or self.in_region(x, y - 1)
        near_region = near_region or self.in_region(x + 1, y + 1) or self.in_region(x - 1, y - 1)
        near_region = near_region or self.in_region(x + 1, y - 1) or self.in_region(x - 1, y + 1)
        return near_region


    def in_region(self, x, y):
        for i in xrange(0, len(self.pixels)):
            curr_pixel = self.pixels[i]
            if curr_pixel.get_x() == x and curr_pixel.get_y() == y:
                return True
        return False
    
    def get_number_of_skin_pixels(self):
        count = 0
        for i in xrange(0, self.size):
            if self.pixels[i].is_skin():
                count += 1
        return count

    def get_average_intensity(self):
        intensities = [pixel.get_intensity() for pixel in self.pixels]
        return sum(intensities)/len(intensities)

    def get_topmost_pixel(self):
        self.pixels.sort(key = operator.attrgetter('x'), reverse=False)
        return self.pixels[0]

    def get_bottommost_pixel(self):
        self.pixels.sort(key = operator.attrgetter('x'), reverse=True)
        return self.pixels[0]

    def get_rightmost_pixel(self):
        self.pixels.sort(key = operator.attrgetter('y'), reverse=False)
        return self.pixels[0]

    def get_leftmost_pixel(self):
        self.pixels.sort(key = operator.attrgetter('y'), reverse=True)
        return self.pixels[0]
