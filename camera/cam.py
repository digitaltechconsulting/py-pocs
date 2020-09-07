import picamera
import time
import sys
sys.path.insert(0,'..')
from logger.log import *
import uuid
import threading

class Cam:
    def __init__(self, length=5,snaps=5,path="."):
        self.length = length #Lenght of video
        self.snaps = snaps   #number of photos
        self.path = path
        self.ids = []
        self.camera = picamera.PiCamera();
        self.logger = Logger();
    def getUniqueFileName(self):
        uid = uuid.uuid4().hex
        fileName = '{path}/{uid}.jpg'.format(path=self.path,uid=uid)
        return fileName
        
    def capture(self):
        self.logger.LogInfo("Capturing photos");
        for i in range(self.length):
            uid = uuid.uuid4().hex
            self.logger.LogInfo(i);
            fileName = '{path}/{uid}.jpg'.format(path=self.path,uid=uid)
            self.camera.capture(fileName)
            self.ids.append(fileName)
        return self.ids
    def captureThread(self):
        th = threading.Thread(target=self.capture,args=())
        self.logger.LogInfo("Starting thread capture")
        th.start();
        self.logger.LogInfo("Started thread capture")
        
    def captureSingle(self):
        self.logger.LogInfo("Capturing single photo");
        fileName = self.getUniqueFileName()
        self.camera.capture(fileName)
        self.logger.LogInfo("Captured {fileName}".format(fileName=fileName));
        return fileName;
        
    
        
        
        

if __name__ == "__main__":
    c = Cam(path="../snaps");
    c.captureThread();
    
        