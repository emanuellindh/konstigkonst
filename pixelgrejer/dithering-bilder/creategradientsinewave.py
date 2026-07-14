from PIL import Image
import numpy as np

im = Image.new("L", [512,512])
width, height = im.size

# for x in range(width):
#     for y in range(height):
#         sin = 400+400*np.sin(x*np.pi/400)
#         if y-sin < 0:
#             im.putpixel([x,y],255)

for x in range(width):
    for y in range(height):
        sin = 128+128*np.sin(x*np.pi/256)
        if y-sin > 0:
            im.putpixel([x,y],int(y-sin))

im.show()
im.save("picture.png")