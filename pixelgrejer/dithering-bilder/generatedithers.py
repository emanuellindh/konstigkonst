# this script scans the canvas.png file for every 8x8 dither and sorts them into folders

from PIL import Image
from matplotlib import cm
import numpy as np
from pathlib import Path
import os


im = Image.open("canvas.png")


def containsBlackPixels(nrBlackPixels, x, y):
    blackPixelsCounter = 0
    for i in range(8):
        for j in range(8):
            if (im.getpixel([x+i,y+j]))[0] == 0:
                blackPixelsCounter = blackPixelsCounter + 1
    return blackPixelsCounter == nrBlackPixels

startingPoint8WaySymmetric = [16,0]
startingPoint2WaySymmetric = [16,144]
startingPointNoSymmetry = [16,288]



# Path("../dithering-bilder/eightway").mkdir(parents=True, exist_ok=True)
# Path("../dithering-bilder/twoway").mkdir(parents=True, exist_ok=True)
# Path("../dithering-bilder/random").mkdir(parents=True, exist_ok=True)

# for i in range(0, 65, 4):
#     Path("../dithering-bilder/eightway/" + str(i)).mkdir(parents=True, exist_ok=True)
#     Path("../dithering-bilder/twoway/" + str(i)).mkdir(parents=True, exist_ok=True)
#     Path("../dithering-bilder/random/" + str(i)).mkdir(parents=True, exist_ok=True)

x = 16
y = 0
finishedRow = False
while (y <= 128):
    finishedRow = False
    i = 1
    os.chdir(Path("../dithering-bilder/eightway/" + str(int(y/2))))
    while (not finishedRow):
        if (sum(im.getpixel([x,y])) == 832):
            x = x + 8
        elif containsBlackPixels(int(y/2),x,y):
            cutout = im.crop([x,y,x+8,y+8])
            cutout.save((str(i) + ".png"))
            i = i + 1
            x = x + 16
            if y == 0:
                y = y + 8
                x = 16
                finishedRow = True
                os.chdir(Path("../../../dithering-bilder"))
        else:
            y = y + 8
            x = 16
            finishedRow = True
            os.chdir(Path("../../../dithering-bilder"))

x = 16
y = 144
finishedRow = False
while (y <= 272):
    finishedRow = False
    i = 1
    os.chdir(Path("../dithering-bilder/twoway/" + str(int((y-144)/2))))
    while (not finishedRow):
        if (sum(im.getpixel([x,y])) == 832):
            x = x + 8
        elif containsBlackPixels(int((y-144)/2),x,y):
            cutout = im.crop([x,y,x+8,y+8])
            cutout.save((str(i) + ".png"))
            i = i + 1
            x = x + 16
            if y == 144:
                y = y + 8
                x = 16
                finishedRow = True
                os.chdir(Path("../../../dithering-bilder"))
        else:
            y = y + 8
            x = 16
            finishedRow = True
            os.chdir(Path("../../../dithering-bilder"))

x = 16
y = 288
finishedRow = False
while (y <= 416):
    finishedRow = False
    i = 1
    os.chdir(Path("../dithering-bilder/random/" + str(int((y-288)/2))))
    while (not finishedRow):
        if (sum(im.getpixel([x,y])) == 832):
            x = x + 8
        elif containsBlackPixels(int((y-288)/2),x,y):
            cutout = im.crop([x,y,x+8,y+8])
            cutout.save((str(i) + ".png"))
            i = i + 1
            x = x + 16
            if y == 288:
                y = y + 8
                x = 16
                finishedRow = True
                os.chdir(Path("../../../dithering-bilder"))
        else:
            y = y + 8
            x = 16
            finishedRow = True
            os.chdir(Path("../../../dithering-bilder"))
        