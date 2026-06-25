from PIL import Image
from matplotlib import cm
import numpy as np
# import pixelgrejer.python.raytracing.geometry as geometry
import geometry as geo

width = 128
height = 128

myCanvas = np.zeros((height, width))
myHitBoxes = np.zeros((height, width))
for i in range(3):
    for j in range(100):
        myHitBoxes[14+j][100+i] = 1
myLines = []
myLines.append(geo.line([100,10],[100,110]))
myLines.append(geo.line([10,10],[30,119]))

lightSource = (64,64)
rays = 1600
energyLossOnHit = 0.9
# energyLossOnHit = 0.001
thresholdToDisappear = 0.01

def hitBox(x,y):
    if x>127 or y>127:
        return True
    elif myHitBoxes[y][x] == 1:
        return True 
    
# checks if path to light source is obstructed or not, if we should count it as a light or shadow
def unobstructed(x, y):
    lineToLight = geo.line([lightSource[0],lightSource[1]],[x,y])
    res = True
    for l in myLines:
        print(l)
        print(lineToLight.startingPoint)
        if geo.intersect(l, lineToLight):
            res = False
    return res

def sendRay(angle, x, y):
    # Xdir = 1
    # Ydir = 1
    movesXdir = np.cos(angle/180*(np.pi))
    movesYdir = np.sin(angle/180*(np.pi))
    Xdir = int(np.sign(movesXdir))
    Ydir = int(np.sign(movesYdir)) # blir 0 när vinkeln är 0
    moves = np.inf
    if movesYdir!=0:
        moves = abs(movesXdir/movesYdir)
    movesLeft = moves

    pointsToCheck = []
    

    # x = lightSource[0]
    # y = lightSource[1]
    intensity = 100

    # hasAlreadyUpdatedIntensity = False
    while intensity > thresholdToDisappear:
        # nextX = x
        # nextY = y
        if(y>=0 and y<height and x>=0 and x<width):
            # myCanvas[y][x] += intensity
            # this added too much noise
            if myCanvas[y][x] < intensity:
                myCanvas[y][x] = intensity

        if movesLeft > 1:
            #should move in x dir
            if hitBox(x+Xdir,y):
                pointsToCheck.append([x,y,intensity])
                Xdir = -1*Xdir
                intensity = intensity*energyLossOnHit
            else:
                x+=Xdir
                movesLeft-=1
        else:
            #should move in y dir
            if hitBox(x,y+Ydir):
                pointsToCheck.append([x,y,intensity])
                Ydir = -1*Ydir
                intensity = intensity*energyLossOnHit
            else:
                y+=Ydir
                movesLeft+=moves

        if (y<0 and Ydir==-1) or (x<0 and Xdir==-1):
            #is the ray moving away from canvas
            intensity = 0
    print(pointsToCheck)
    print(len(pointsToCheck))
    intensityTotal = 0
    for i in range(len(pointsToCheck)):
        if unobstructed(pointsToCheck[i][0],pointsToCheck[i][1]):
            intensity+=pointsToCheck[i][2]

            

    # print("movesXdir: ", movesXdir)
    # print("movesYdir: ", movesYdir)
    # print("Xdir: ", Xdir)
    # print("Ydir: ", Ydir)
    # print("moves: ", moves)
    # print("x: ", x)
    # print("y: ", y)

# for i in range(rays):
#     angle = i*360/rays
#     # print("angle: ", angle)
#     sendRay(angle)

for i in range(width):
    for j in range(height):
        # angleToLightSource=np.atan2((lightSource[1]-j), (lightSource[0]-i))
        # print("x: ", i)
        # print("y: ", j)
        # print("angle: ", angleToLightSource)
        # myCanvas[j][i] = 128 + angleToLightSource*(128/np.pi)
        # angleInDegrees = angleToLightSource*(180/np.pi)
        # if i == 10 and j == 10:
        #     sendRay(angleInDegrees, i, j)
        if unobstructed(i,j):
            # print("au")
            myCanvas[j][i] = 128

# #add another light source
# lightSource = (10,100)
# for i in range(rays):
#     angle = i*360/rays
#     # print("angle: ", angle)
#     sendRay(angle)



# im = Image.fromarray(np.uint8(cm.gist_earth(myarray)*255))
im = Image.fromarray(myCanvas)

im = im.convert('RGB')
im.save("rt.png")
