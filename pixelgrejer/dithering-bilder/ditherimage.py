import os
from pathlib import Path
from PIL import Image
import numpy as np

im = Image.open("picture.png")

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

for x in range(0,width,8):
    for y in range(0,height,8):
        intensity = intensityOfRegion(x,y)
        intensity = int(intensity/16)
        nrOfDithersToChooseFrom = nrOfDithers[intensity]
        chosenDither = np.random.choice(nrOfDithersToChooseFrom) + 1
        # print(intensity)
        # print(nrOfDithersToChooseFrom)
        # print(chosenDither)
        # print("-")
        dither = Image.open("eightway/" + str(intensity*4) + "/" + str(chosenDither) + ".png")
        # dither.show()
        im.paste(dither,[x,y])

im.show()
im.save("ditheredpicture.png")