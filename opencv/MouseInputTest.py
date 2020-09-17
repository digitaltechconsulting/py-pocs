import numpy as np
import cv2
class MouseInputTest:
    def __init__(self,imageName='testWindow',registerMouseEvents=False):
        print("initializing cam")
        self.cap = cv2.VideoCapture(0)
        print("initializing cam done")
        self.imageName = imageName
        self.registerMouseEvents = registerMouseEvents
    def onMouse(self,event,x,y,flags,param):
        print(f"({x},{y})")
    def RegisterMouseCallBack(self):
        if self.registerMouseEvents == True:
            print('Registering mouse call back')
            cv2.setMouseCallback(self.imageName,self.onMouse)
            print('Registering mouse call back - Complete')


    def StartCam(self):
        first = True
        while True:
            _ , pic = self.cap.read()
            cv2.imshow(self.imageName,pic)
            if self.registerMouseEvents == True and first == True:
                self.RegisterMouseCallBack()
                first = False
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

if __name__ == "__main__":
    m = MouseInputTest(registerMouseEvents=True)
    m.StartCam()
    print("Exiting....")