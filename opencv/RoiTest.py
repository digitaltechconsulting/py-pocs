import numpy as np
import cv2
class RoiTest:
    def __init__(self):
        print('inside constructor')
        self.path = f"C:\\data\\code\\python\\py-pocs\\opencv\\aaroh_four.jpeg"
        print(self.path)

    def __del__(self):
        pass
    def Test(self):
        img = cv2.imread(self.path)
        print(img.shape)
        img = img[:,:,0:1]
        print(img.shape)

        cv2.imshow("test",img)
        cv2.imread("test",)

        cv2.setMouseCallback('test',self.click_event)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def click_event(self,event,x,y,flags,param):
        #msg = f"({x},{y})"
        #print(msg)
        pass
if __name__ == "__main__":
    o = RoiTest()
    o.Test()
