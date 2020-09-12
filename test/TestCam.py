import cv2
import numpy as np

class TestCam:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    def __del__(self):
        self.cap.release()
    def Capture(self):
        while(True):
            ret,pic = self.cap.read()
            gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY) 
            cv2.imshow("Picture",gray)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    def CaptureImage(self):
        img = cv2.imread("test.jpg",1)
        cv2.imshow("test",img)
        cv2.waitKey(0) 
        cv2.destroyAllWindows() 
    def ImgUsingNumPy(self):
        img = np.zeros([512,512,3],np.uint8)
        cv2.imshow('Numpi img',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def VideoCaptureTest(self):
        self.PrintResoluton()
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,3000)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,3000)
        self.PrintResoluton()
        cv2.namedWindow('fullScreen',cv2.WINDOW_NORMAL)
        while True:
            ret,img = self.cap.read()
            textImg = cv2.putText(img,"Hello World",(10,50))
            cv2.imshow('fullScreen',img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    def PrintResoluton(self):
        width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print("Rsolution is {width}x{height}".format(height=height,width=width))
if __name__ == "__main__":
    t = TestCam()
    #t.Capture()
    #t.CaptureImage()
    #t.ImgUsingNumPy()
    t.VideoCaptureTest()
    
#How to draw shapes 5:20:34
#Set cap properties