import numpy as np
import cv2
class MouseInputTest:
    def __init__(self,name="aaroh_four.jpeg",imageName='aaroh_four.jpeg'):
        self.fileName = name
        self.imageName = imageName
        self.img = cv2.imread(self.fileName)
        print(f"image shape is : {self.img.shape}")
        #print(f"Image is : {self.img}")
        #print(f"ravel(): {self.img.ravel()}")
        cv2.imshow(self.imageName,self.img)
        cv2.setMouseCallback(self.imageName,self.click_event)
        self.fontFace = cv2.FONT_HERSHEY_SIMPLEX
        self.fontScale = 1
        self.thickness = 2
    def click_event(self,event,x,y,flags,param):
        msg = f"({x},{y})"
        picWithImg = self.PutText(msg,50,50)
        cv2.imshow(self.imageName,picWithImg)

        pass
    def PutText(self,msg,x,y):
        picWithText = cv2.putText(
            self.img,
            msg, (x,y),
            self.fontFace,
            self.fontScale,
            (255,255,0),
            self.thickness
        )
        return picWithText

if __name__ == "__main__":
    m = MouseInputTest()
    cv2.waitKey(0)
    cv2.putText()
    cv2.destroyAllWindows()
