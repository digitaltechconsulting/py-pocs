# Time 2:35
#Hue corresponds to the color components ( base pigment )
#HSV Hue Saturation Value
#HSV is also known as Hue Saturation Value 
#Hue is a single value that represents color

#Hue : color in degree ( 0 to 360 degree )
#Saturation: How far it is from the center (0-1 Dominance of Hue (center to outer))
#Value/Brightness: 0 to 1 

#there are 150 conversion methods and one of then is coloured to HSV
import cv2 as cv
import numpy as np

class HSVObjectDetection:
    def __init__(self):
        print("Initializing camera...")
        self.cap = cv.VideoCapture(0)
        print("Camera initialized...")
        self.mainWindow = "mainWindow"
        self.trackingWindow = 'trackingWindow'
        self.maskWindow = 'maskedWindow'
        cv.namedWindow(self.mainWindow)
        cv.namedWindow(self.trackingWindow)
        cv.namedWindow(self.maskWindow)
        
        
        pass
    def __del__(self):
        pass
    def BeginDemo(self):
        while True:
            _,frame = self.cap.read()
            hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
            l_b = np.array([110,50,50]) #hsv for blue
            u_b = np.array([130,255,255])

            mask = cv.inRange(hsv, l_b,u_b)
            cv.imshow(self.maskWindow,mask)

            res = cv.bitwise_and(frame,frame,mask=mask)

            cv.imshow(self.mainWindow,hsv)
            cv.imshow('res',res)
            if cv.waitKey(1) == 27:
                break
        pass


if __name__ == "__main__":
    o = HSVObjectDetection()
    o.BeginDemo()
    print("destroying all windows")
    cv.destroyAllWindows()