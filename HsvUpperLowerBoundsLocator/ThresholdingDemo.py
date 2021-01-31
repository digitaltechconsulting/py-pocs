#2:54

import cv2 as cv
import  numpy as np

path = "C:\\data\\code\\python\\py-pocs\\Tutorials\\balls.jpg"

img = cv.imread(path)
print(img.shape)
print(img[100,100])
img[719,100] = [255,255,255]
cv.imshow("image",img)

t = img.item(10,10,1)
y = 10 
x = 10
print(f'Accessing pixel by img.item {img.item(,1)}')

cv.waitKey(5000)
cv.destroyAllWindows()

