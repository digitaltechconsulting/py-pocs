import numpy as np
import cv2 as cv

class TrackBarSwitchDemo:
    def __init__(self):
        print('Inside constructor')
        self.winname = "MainWindow"

        #Not working
        cv.namedWindow(self.winname)
        #cv.setWindowProperty(self.winname,cv.WND_PROP_FULLSCREEN,cv.WINDOW_FULLSCREEN)
        print('Initializing camera') 
        self.cap = cv.VideoCapture(0)
        print('Initializing camera done') 
    def __del__(self):
        print('Inside destructor')
        self.Dispose()
    def Dispose(self):
        cv.destroyAllWindows()
        self.cap.release()

    def Entry(self):
        cv.createTrackbar('test',self.winname,0,255,self.onChange)
        switch='Gray scaled?'
        cv.createTrackbar(switch,self.winname,0,1,self.onChange)
        while(1):
            _,frame = self.cap.read()
            switchValue = cv.getTrackbarPos(switch,self.winname)
            if switchValue == 1:
                frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
            else:
                print('Coloured')
            cv.imshow(self.winname,frame)
            key = cv.waitKey(1)
            if ord('a') == key:
                break
        pass
    def onChange(self,x):
        print(f'Value is : {x}')

if __name__ == "__main__":
    t = TrackBarSwitchDemo()
    t.Entry()
    t.Dispose()