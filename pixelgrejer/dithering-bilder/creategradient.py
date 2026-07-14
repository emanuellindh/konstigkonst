from PIL import Image
import numpy as np

# im = Image.new("L", [272,256])

# for i in range(0,272,16):
#     print(i)
#     im2 = Image.new("L", [16,256], 256-i)
#     im.paste(im2,[i,0])

im = Image.open("ex.png")
im = im.convert("L")
width, height = im.size
im = im.crop([0,0,np.floor(width/8)*8,np.floor(height/8)*8])
width, height = im.size


def intensityAtPixel(x,y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return 0, True
    else:
        return im.getpixel([x,y]), False
    
im2 = im.copy()

# for x in range(width):
#     for y in range(height):
#         totalIntensity = 0
#         nrPixels = 0
#         for i in range(-3,4,1):
#             for j in range(-3,4,1):
#                 intensity, outOfBounds = intensityAtPixel(x+i,y+j)
#                 if not outOfBounds:
#                     totalIntensity += intensity
#                     nrPixels += 1
#         finalIntensity = int(totalIntensity/nrPixels)
#         

for x in range(width):
    for y in range(height):
        intensity, outOfBounds = intensityAtPixel(x,y)
        difference = int((128-intensity)/2)
        im2.putpixel([x,y],intensity-difference)

maxValue = im2.getextrema()
print(maxValue)

im2.show()
im2.save("picture.png")