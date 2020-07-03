#import library
from PIL import Image
import numpy as np

#Load the image
img = Image.open('/Users/patricianaccachian/AR-SL-MAP/tunnelbana.png')
imga = img.convert("RGBA")
datas = imga.getdata()
matrix = np.array(img.getdata())

print (matrix)

newData = []
for item in datas:
    #Added a range because sometimes the number of the pixel I want transparent isn't exactly 255
    if (250 <= item[0] <= 255) and (250 <= item[1] <= 255) and (250 <= item[2] <= 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
        print(item)

img.putdata(newData)
img.save("/Users/patricianaccachian/AR-SL-MAP/stockholm-metro-map.png")