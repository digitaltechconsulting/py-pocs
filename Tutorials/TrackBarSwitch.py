import numpy as np
import cv2 as cv

class TrackBarSwitchDemo:
    def __init__(self):
        print('Inside constructor')
        self.winname = "MainWindow"
        cv.namedWindow(self.winname,cv.CV_WINDOW_NORMAL)
        cv.setWindowProperty(self.winname,cv.WND_PROP_FULLSCREEN,cv.WINDOW_FULLSCREEN)
        print('Initializing camera') 
        self.cap = cv.VideoCapture(0)
        print('Initializing camera done') 
        pass
    def __del__(self):
        print('Inside destructor')
        cv.destroyAllWindows()
        self.cap.release()
        pass
    def Entry(self):
        cv.createTrackbar('test',self.winname,0,255,self.onChange)
        while(1):
            _,frame = self.cap.read()
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