import picamera
import time
import sys
sys.path.insert(0,'..')
from logger.log import *
import uuid

class Cam:
    def __init__(self, length=5,snaps=5):
        self.length = length
        self.snaps = snaps
        self.camera = picamera.PiCamera();
        self.logger = Logger();
    def capture(self):
        self.logger.LogInfo("Capturing photos");
        for i in range(self.length):
            uid = uuid.uuid4().hex
            self.logger.LogInfo(i);
            fileName = '{uid}.jpg'.format(uid=uid)
            self.camera.capture(fileName)
        
        
        

if __name__ == "__main__":
    c = Cam();
    c.capture();
    
        