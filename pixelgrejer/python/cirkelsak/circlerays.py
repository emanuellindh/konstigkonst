from PIL import Image
# import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import sympy as sp
from sympy.solvers import solve



height = 1080
length = 1920

myarray = np.zeros((height,length))

circlePos = [height,length/2]
circleRadius = 400

# startingPoint = [length/2,height]
def outOfBounds(y,x):
    if x < 0 or x >= length or y < 0 or y >= height:
        return True


for i in range(height-1-circleRadius,0,-1):
# for i in range(height):
    # print(i)
    coordinate = [i,length/2]
    # print(coordinate)
    colour = 255*i/(height-circleRadius)

    x,y = sp.symbols('x, y')
    
    eq1 = sp.Eq((coordinate[0]-x)*(circlePos[0]-x)+(coordinate[1]-y)*(circlePos[1]-y),0)
    eq2 = sp.Eq((circlePos[0]-x)**2 + (circlePos[1]-y)**2 - circleRadius**2,0)
    output = solve([eq1,eq2],dict=True)
    values = list(output[0].values())
    # print(values)

    directionVector=np.subtract(values,coordinate)
    # print(directionVector)
    magnitude = directionVector[0]**2+directionVector[1]**2
    # magnitude = np.hypot(directionVector[0],directionVector[1])
    magnitude = sp.sqrt(magnitude)
    directionVector=np.divide(directionVector,magnitude)
    # print(directionVector)

    myarray[int(values[0])][int(values[1])] = 255
    myarray[int(coordinate[0])][int(coordinate[1])] = 255

    while not(outOfBounds(coordinate[0],coordinate[1])):
        myarray[int(coordinate[0])][int(coordinate[1])] = 255-colour
        coordinate = coordinate + directionVector

# myarray[100][200] = 255
        

im = Image.fromarray(myarray)

im = im.convert('RGB')
im.save("gr.png")
