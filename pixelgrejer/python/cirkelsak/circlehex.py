from PIL import Image
# import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import sympy as sp
from sympy.solvers import solve



height = 1080
length = 1920

myarray = np.zeros((height,length))

circlePos = [height/2,length/2]

circleOuterRadius = 400
circleInnerRadius = np.sqrt(3)*circleOuterRadius/2

for i in range(height):
    for j in range(length):
        # if (np.sqrt((circlePos[0]-i)**2+(circlePos[1]-j)**2) < circleInnerRadius):
        #     myarray[i][j] = 255
        # elif (np.sqrt((circlePos[0]-i)**2+(circlePos[1]-j)**2) > circleOuterRadius):
        #     myarray[i][j] = 0
        # else:
            distance = np.sqrt((circlePos[0]-i)**2+(circlePos[1]-j)**2)-circleInnerRadius
            ratio = distance/(circleOuterRadius-circleInnerRadius)
            colour = ratio*255
            myarray[i][j] = colour


im = Image.fromarray(myarray)

im = im.convert('RGB')
im.save("gr.png")
