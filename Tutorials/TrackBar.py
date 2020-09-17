#time 2:30
import numpy as np
import cv2

def noting(x):
    print(x)
windowName = 'image'
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar("b",windowName,0,255,noting)
cv2.createTrackbar("g",windowName,0,255,noting)
cv2.createTrackbar("r",windowName,0,255,noting)
while True:
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    b = cv2.getTrackbarPos("b",windowName)
    g = cv2.getTrackbarPos("g",windowName)
    r = cv2.getTrackbarPos("r",windowName)
    img[:] = [b,g,r]

cv2.destroyAllWindows()
