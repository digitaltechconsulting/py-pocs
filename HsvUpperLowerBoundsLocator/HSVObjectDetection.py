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
        self.path = "C:\\data\\code\\python\\py-pocs\\HsvUpperLowerBoundsLocator\\balls.jpg"
        self.cap = cv.VideoCapture(0)
        print("Camera initialized...")
        self.mainWindow = "mainWindow"
        self.trackingWindow = 'trackingWindow'
        self.maskWindow = 'maskedWindow'
        
        cv.namedWindow(self.mainWindow)
        cv.namedWindow(self.trackingWindow)
        cv.namedWindow(self.maskWindow)

        cv.createTrackbar('LH',self.trackingWindow,0,255,self.onChange)
        cv.createTrackbar('LS',self.trackingWindow,0,255,self.onChange)
        cv.createTrackbar('LV',self.trackingWindow,0,255,self.onChange)
        cv.createTrackbar('UH',self.trackingWindow,255,255,self.onChange)
        cv.createTrackbar('US',self.trackingWindow,255,255,self.onChange)
        cv.createTrackbar('UV',self.trackingWindow,255,255,self.onChange)
        
    def __del__(self):
        pass
    def onChange(self,x):
        pass
    def BeginDemo(self):
        while True:
            _,frame = self.cap.read()
            #frame =  cv.imread(self.path)
            hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

            lHb = cv.getTrackbarPos('LH',self.trackingWindow)
            lSb = cv.getTrackbarPos('LS',self.trackingWindow)
            lVb = cv.getTrackbarPos('LV',self.trackingWindow)

            uHb = cv.getTrackbarPos('UH',self.trackingWindow)
            uSb = cv.getTrackbarPos('US',self.trackingWindow)
            uVb = cv.getTrackbarPos('UV',self.trackingWindow)

            l_b = np.array([lHb,lSb,lVb]) #hsv for blue
            u_b = np.array([uHb,uSb,uVb])

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