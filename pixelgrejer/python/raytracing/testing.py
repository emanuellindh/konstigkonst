from PIL import Image
from matplotlib import cm
import numpy as np
# import pixelgrejer.python.raytracing.geometry as geometry
import geometry as geo

width = 128
height = 128

myCanvas = np.zeros((height, width))
myHitBoxes = np.zeros((height, width))
points = [[50,50],[50,100],[100,50]]

def distanceToPoint(p1,p2):
    return (np.abs(p1[0]-p2[0])+np.abs(p1[1]-p2[1]))

for i in range(width):
    for j in range(height):
        value = 0
        for k in range(3):
            value += distanceToPoint([i,j],points[k])
        if value>120:
            myCanvas[j][i] = value


im = Image.fromarray(myCanvas)

im = im.convert('RGB')
im.save("rt.png")
