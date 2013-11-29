from __future__ import division
from colorsys import *

class Pixel:
    def __init__(self, x, y, red, green, blue):
        self.x = x
        self.y = y
        self.red = red
        self.green = green
        self.blue = blue
        self.region = None

    @property
    def region(self):
        return self.region
    @region.setter
    def region(self, value):
        self.region = value

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    def in_region(self):
        if self.region == None:
            return False
        else:
            return True

    def is_skin(self):
        r = self.red
        g = self.green
        b = self.blue
        rgbClassifier = ((r > 95) and (g > 40 and g < 100) and (b > 20) and ((max(r, g, b) - min(r, g, b)) > 15) and (abs(r-g) > 15) and (r > g) and (r > b))
        normalizedRGBClassifier = False
        if r != 0 and g != 0 and b != 0:
            normR = (r/(r + g + b))
            normG = (g/(r + g + b))
            normB = (b/(r + g + b))
            normalizedRGBClassifier = (((normR/normG) > 1.185) and (((r * b)/(pow(r + g + b, 2))) > 0.107) and (((r * g)/(pow(r + g + b,2))) > 0.112))
        hsv = rgb_to_hsv(r, g, b)
        hsvClassifier = (hsv[0] > 0 and hsv[0] < 35 and hsv[1] > 0.23 and hsv[1] < 0.68)
        return (rgbClassifier or normalizedRGBClassifier or hsvClassifier)

    def intensity(self):
        return (self.red + self.green + self.blue)/3
