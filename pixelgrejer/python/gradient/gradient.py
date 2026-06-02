from PIL import Image
# import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

myarray = np.zeros((128,128))
myarray2 = np.ones((1024,1024))
for i in range(128):
    # myarray[i] = np.ones(1024)*(i/4)
    # if (i!=0):
        # myarray[i] = list(map(lambda x: x**(i/256), np.arange(-512,512,1)/128))
        # myarray[i] = list(map(lambda x: x**(i+64), np.arange(-64,64,1)/2048 + np.ones(128)))
        myarray[i] = list(map(lambda x: x**(i), np.arange(-64,64,1)/16)) + np.ones(128)

myarray = myarray*16
print(myarray)

def sq(x):
    return x*x

mylist = np.arange(0,10,1)
print(mylist)
# mylist = list(map(sq, mylist))
mylist = list(map(lambda x: x**3, mylist))
print(mylist)
print(0.995**0.75)



# im = Image.fromarray(np.uint8(cm.gist_earth(myarray)*255))
im = Image.fromarray(myarray)


# im.show()
im = im.convert('RGB')
im.save("gr.png")
