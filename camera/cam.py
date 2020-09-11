import cv2
import time
import sys
sys.path.insert(0,'..')
from logger.log import *
import uuid
import threading

class Cam:
    def __init__(self, length=5,snaps=5,path="."):
        self.logger = Logger()
        self.length = length #Lenght of video
        self.snaps = snaps   #number of photos
        self.path = path
        self.ids = []
        self.logger.LogInfo('Loading camera...')
        self.camera = cv2.VideoCapture(0)
        self.logger.LogInfo('Camera loaded successfully...')
    def __del__(self):
        self.logger.LogInfo("Releasing resources...")
        if self.camera != None:
            self.camera.release()
    def getUniqueFileName(self):
        uid = uuid.uuid4().hex
        fileName = '{path}/{uid}.jpg'.format(path=self.path,uid=uid)
        return fileName
        
    def captureSingle(self,path=""):
        self.logger.LogInfo("Capturing single photo");
        if path == "":
            self.logger.LogInfo("Path not provided using default -> {path}".format(path=self.path))
        else:
            self.path = path
            self.logger.LogInfo("Path not provided using default -> {path}".format(path=path))
        print("About to take picture....")    
        fileName = self.getUniqueFileName()
        while(True):
            ret,img = self.camera.read()
            cv2.imwrite(fileName,img)
            break
        self.logger.LogInfo("Captured {fileName}".format(fileName=fileName));
        return fileName
if __name__ == "__main__":
    c = Cam(path="../snaps")
    c.captureSingle(path=".")
    c.captureSingle(path=".")
    c.captureSingle(path=".")
    c.captureSingle(path=".")
    
        