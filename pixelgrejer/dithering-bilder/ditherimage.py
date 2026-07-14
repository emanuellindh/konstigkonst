import os
from pathlib import Path
from PIL import Image
import numpy as np

im = Image.open("picture.png")
im2 = im.copy()
im2 = im2.convert("RGB")

nrOfDithers = []
for i in range(0,65,4):
    lst = os.listdir(Path("../dithering-bilder/eightway/" + str(i)))
    number_files = len(lst)
    nrOfDithers = nrOfDithers + [number_files]
# print(nrOfDithers)

width, height = im.size
# print(width)

def intensityOfRegion(x,y):
    result = 0
    for i in range(8):
        for j in range(8):
            result = result + im.getpixel([x+i,y+j])
    return result/64

def colorize(dither):
    for i in range(8):
        for j in range(8):
            if dither.getpixel([i,j])[0] == 0:
                # dither.putpixel([i,j],(81,176,136)) # mörkgrön
                # dither.putpixel([i,j],(21,75,150)) # mörkblå
                dither.putpixel([i,j],(151,107,255)) # ljuslila
            else:
                # dither.putpixel([i,j],(186,255,226)) # ljusgrön
                # dither.putpixel([i,j],(66,31,148)) # lila
                dither.putpixel([i,j],(101,36,255)) # mörklila


for x in range(0,width,8):
    for y in range(0,height,8):
        intensity = intensityOfRegion(x,y)+8
        intensity = int(intensity/16)
        nrOfDithersToChooseFrom = nrOfDithers[intensity]
        chosenDither = np.random.choice(nrOfDithersToChooseFrom) + 1
        # print(intensity)
        # print(nrOfDithersToChooseFrom)
        # print(chosenDither)
        # print("-")
        dither = Image.open("eightway/" + str(intensity*4) + "/" + str(chosenDither) + ".png")
        # dither.show()
        colorize(dither)
        im2.paste(dither,[x,y])

im2.show()
im2.save("ditheredpicture.png")