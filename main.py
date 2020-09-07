from camera.cam import *
from logger.log import *
import RPi.GPIO as GPIO
import threading
import time
import os
import camera.cam as cam

MOTION_SENSOR_PIN = 11

class Main:
    def __init__(self):
        self.logger = Logger()
        self.motionDetected = False
        self.MotionDetectorThread = None
        self.cam = cam.Cam(path="./snaps")
        self.capturedFiles = []
    def Entry(self):
        self.logger.LogInfo("Inside Entry....")
        #c = Cam(5,5,path="./snaps")
        #ids = c.capture()
        #print(ids)
        self.StartMotionDetector()
    def StartMotionDetector(self):
        self.logger.LogInfo("Setting up GPIO pins");
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)
        self.MotionDetectorThread = threading.Thread(target=self.StartMotionDetectorThread,args=())
        self.logger.LogInfo("Starting StartMotionDetectorThread");
        self.MotionDetectorThread.start()
    def StartMotionDetectorThread(self):
        self.logger.LogInfo("Started StartMotionDetectorThread");
        while True:
            if GPIO.input(MOTION_SENSOR_PIN) == GPIO.HIGH:
                if self.motionDetected == False:
                    #start taking pics
                    self.motionDetected = True
                    self.logger.LogInfo("Motion has detected and taking snaps");
                else:
                    fileName = self.cam.captureSingle();
                    self.capturedFiles.append(fileName)
                    time.sleep(1)
            else:
                if self.motionDetected == True:
                    self.logger.LogInfo("Cleaning up stuff.");
                    self.motionDetected = False
                    self.logger.LogInfo(self.capturedFiles)
                    for f in self.capturedFiles:
                        os.remove(f)
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