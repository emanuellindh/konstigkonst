# render a 3d object defined by points

from PIL import Image
import numpy as np


im = Image.new("RGB", [512,512])
width, height = im.size

backgroundcolor = [0,0,0]

class polygon3d:
    # points = []
    def __init__(self, points):
        self.points = points


for x in range(width):
    for y in range(height):
        im.putpixel([x,y],int(y))

pol1 = polygon3d([[30,20],[30,10,33]])

print(pol1.points)

im.show()
im.save("picture.png")