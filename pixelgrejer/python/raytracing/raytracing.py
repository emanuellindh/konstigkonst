from PIL import Image
from matplotlib import cm
import numpy as np

myCanvas = np.zeros((128,128))
myHitBoxes = np.zeros((128,128))
for i in range(3):
    for j in range(100):
        myHitBoxes[14+j][100+i] = 1

lightSource = (-10,100)
rays = 1600
energyLossOnHit = 0.9
thresholdToDisappear = 0.01

def hitBox(x,y):
    if x>127 or y>127:
        return True
    elif myHitBoxes[y][x] == 1:
        return True 

def sendRay(angle):
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
    

    x = lightSource[0]
    y = lightSource[1]
    intensity = 100

    # hasAlreadyUpdatedIntensity = False
    while intensity > thresholdToDisappear:
        # nextX = x
        # nextY = y
        if(y>0 and y<127 and x>0 and x<127):
            # myCanvas[y][x] += intensity
            # this added too much noise
            if myCanvas[y][x] < intensity:
                myCanvas[y][x] = intensity

        if movesLeft > 1:
            #should move in x dir
            if hitBox(x+Xdir,y):
                Xdir = -1*Xdir
                intensity = intensity*energyLossOnHit
            else:
                x+=Xdir
                movesLeft-=1
        else:
            #should move in y dir
            if hitBox(x,y+Ydir):
                Ydir = -1*Ydir
                intensity = intensity*energyLossOnHit
            else:
                y+=Ydir
                movesLeft+=moves

        if (y<0 and Ydir==-1) or (x<0 and Xdir==-1):
            #is the ray moving away from canvas
            intensity = 0
            

    # print("movesXdir: ", movesXdir)
    # print("movesYdir: ", movesYdir)
    # print("Xdir: ", Xdir)
    # print("Ydir: ", Ydir)
    # print("moves: ", moves)
    # print("x: ", x)
    # print("y: ", y)

for i in range(rays):
    angle = i*360/rays
    # print("angle: ", angle)
    sendRay(angle)

# #add another light source
# lightSource = (10,100)
# for i in range(rays):
#     angle = i*360/rays
#     # print("angle: ", angle)
#     sendRay(angle)

# for i in range(128):
#     myCanvas[i] = np.ones(128)*(i*2)

# def sq(x):
#     return x*x



# im = Image.fromarray(np.uint8(cm.gist_earth(myarray)*255))
im = Image.fromarray(myCanvas)


# im.show()
im = im.convert('RGB')
im.save("rt.png")
