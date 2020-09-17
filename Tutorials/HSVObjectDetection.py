# Time 2:35
#Hue corresponds to the color components ( base pigment )
#HSV Hue Saturation Value
#HSV is also known as Hue Saturation Value 
#Hue is a single value that represents color

#Hue : color in degree
#Saturation: How far it is from the center
#Value/Brightness: 


import cv2 as cv
import numpy as np

class HSVObjectDetection:
    def __init__(self):
        print("Initializing camera...")
        self.cap = cv.VideoCapture(0)
        print("Camera initialized...")
        self.mainWindow = "mainWindow"
        pass
    def __del__(self):
        pass
    def BeginDemo(self):
        while True:
            _,frame = self.cap.read()
            hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
            cv.imshow(self.mainWindow,hsv)
            if cv.waitKey(1) == 27:
                break
        pass


if __name__ == "__main__":
    o = HSVObjectDetection()
    o.BeginDemo()
    print("destroying all windows")
    cv.destroyAllWindows()