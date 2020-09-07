from camera.cam import *

class Main:
    def Entry(self):
        c = Cam(5,5)
        c.capture()
        
        
if __name__ == "__main__":
    print("Running main")
    main = Main();
    main.Entry();