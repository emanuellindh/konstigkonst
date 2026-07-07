from PIL import Image

im = Image.new("L", [272,256])

for i in range(0,272,16):
    print(i)
    im2 = Image.new("L", [16,256], 256-i)
    im.paste(im2,[i,0])

im.show()
# im = im.convert('RGB')
im.save("picture.png")