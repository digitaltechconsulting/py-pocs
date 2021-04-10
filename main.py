from camera.cam import *
from logger.log import *
import RPi.GPIO as GPIO
import threading
import time
import datetime
import os
import camera.cam as cam

import models.MotionParams as MP

MOTION_SENSOR_PIN = 11
imageStore = "./snaps"

class Main:
    def __init__(self):
        self.logger = Logger()
        self.motionDetected = False
        self.motionDetectedTime = None
        self.MotionDetectorThread = None
        self.cam = cam.Cam(path=imageStore)
        self.capturedFiles = []
    def Entry(self):
        self.logger.LogInfo("Inside Entry....")        
        #c = Cam(5,5,path="./snaps")
        #ids = c.capture()
        #print(ids)
        self.StartMotionDetector()
    def StartMotionDetector(self):
        self.SetupGpioPins()
        self.MotionDetectorThread = threading.Thread(target=self.StartMotionDetectorThread,args=())
        self.logger.LogInfo("Starting StartMotionDetectorThread");
        self.MotionDetectorThread.start()
    def SetupGpioPins(self):
        self.logger.LogInfo("Setting up GPIO pins");
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)
        
    def StartMotionDetectorThread(self):
        self.logger.LogInfo("Started StartMotionDetectorThread");
        while True:
            if GPIO.input(MOTION_SENSOR_PIN) == GPIO.HIGH:
                if self.motionDetected == False:
                    #start taking pics
                    mdp = MP.MotionParams()
                    self.motionDetected = True
                    #self.motionDetectedTime = datetime.datetime.now()
                    self.logger.LogInfo("Motion has detected and taking snaps");
                else:
                    newImageStore = "{imageStore}/{motionDetectedTime}".format(imageStore=imageStore,motionDetectedTime=mdp.when)
                    if os.path.exists(newImageStore) == False:
                        os.makedirs(newImageStore)
                    fileName = self.cam.captureSingle(path=newImageStore)
                    self.capturedFiles.append(fileName)
                    time.sleep(0.2)
            else:
                if self.motionDetected == True:
                    self.logger.LogInfo("Cleaning up stuff.")
                    self.motionDetected = False
                    self.logger.LogInfo(self.capturedFiles)
                    for f in self.capturedFiles:
                        #os.remove(f)
                        print("deleting {f}".format(f=f))
                    self.capturedFiles.clear()
                
        
        
if __name__ == "__main__":
    try:
        main = Main();
        main.Entry();
        print("Waiting for threads to join")
        time.sleep(5000)
        main.MotionDetectorThread.join()
        print("Thread joined");
    except KeyboardInterrupt:
        print("Cleaning up GPIO pins");
        GPIO.cleanup()



#test