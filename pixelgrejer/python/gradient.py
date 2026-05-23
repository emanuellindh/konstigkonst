from PIL import Image
# import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
myarray = np.zeros((1024,1024))
for i in range(1024):
    myarray[i] = np.ones(1024)*(i/4)



# im = Image.fromarray(np.uint8(cm.gist_earth(myarray)*255))
im = Image.fromarray(myarray)

im.show()
im = im.convert('RGB')
im.save("gr.png")
