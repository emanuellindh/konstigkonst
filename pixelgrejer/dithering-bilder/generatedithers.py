# this script scans the canvas.png file for every 8x8 dither and sorts them into folders

from PIL import Image
from matplotlib import cm
import numpy as np

im = Image.open("canvas.png")

print(im.getpixel([1,1]))
print(im.getpixel([33,1]))
print(im.getpixel([1,17]))
print(im.getpixel([1,33]))
print(im.getpixel([1,49]))
print(im.getpixel([1,65]))
print(im.getpixel([1,1]))
print(im.getpixel([1,1]))

cutout = im.crop([48,8,56,16])
im.paste(cutout,[500,500])

im.show()
# im = im.convert('RGB')
# im.save("rt.png")



startingPoint8WaySymmetric = [16,8]
startingPoint2WaySymmetric = [16,152]
startingPointNoSymmetry = [16,296]

i = 4
j = 0
while (i <= 60):
    d = 2
    i = i + 4