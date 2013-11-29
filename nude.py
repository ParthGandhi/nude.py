import operator
import argparse
import sys
sys.path.insert(0, 'src/')

import Image
from Pixel import * 
from Region import *
from utils import *

def contains_nudity(image_path):
    image = Image.open(image_path)
    imgPixels = image.load()
    width = image.size[0]
    height = image.size[1]
    pixels = [ [None]*height for i in range(width) ]

    for i in xrange(0, width):
        for j in xrange(0, height):
            pixels[i][j] = Pixel(i, j, imgPixels[i,j][0], imgPixels[i,j][1], imgPixels[i,j][2])
    
    skin_pixels = []
    skin_regions = []
    create_skin_regions(pixels, skin_pixels, skin_regions, width, height)

    if len(skin_regions) < 3:
        return False
    skin_regions.sort(key = operator.attrgetter('size'), reverse=True)

    bounding_region = create_bounding_region(pixels, skin_regions, width, height)
    return analyze_regions(skin_pixels, skin_regions, bounding_region, width, height)

def color_skin(image_path):
    save_path = image_path[:-4] + "-skinified.jpg"
    color_skin_regions(image_path, save_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Detect nudity in images.')
    parser.add_argument('filename', type=str, nargs=1)
    parser.add_argument('-c', action='store_true')
    args = parser.parse_args()
    if args.c is True:
        color_skin(args.filename[0])
        print "Skin regions covered in image saved at " + args.filename[0][:-4] + "-skinified.jpeg"
    else:
        nudity = contains_nudity(args.filename[0])
        if nudity:
           print "Image contains nudity"
        else:
            print "Image doesn't contain nudity"
