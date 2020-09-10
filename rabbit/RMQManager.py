import inspect
import pika
import sys
sys.path.insert(0,'..')
from logger.log import *


class RMQManager:
    def __new__(self,host):
        funcName = inspect.currentframe().f_code.co_name
        self.logger = Logger()
        self.logger.LogInfo(funcName)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        print('Object created')
        
    #def __init__(self):
    #    print("I am in __init__.")
    #    self.test = 1
    def SendMessage(self):
        channel = self.connection.channel()

    def Close(self):
        self.connection.close()

class Test:
    def __new__(self):
        print("inside main")
        return self
    def Hello(self):
        print("Inside hello")

if __name__ == "__main__":
    print("I am in inside RMQManager")
    #r = RMQManager(host="192.168.1.115")
    #r.Close()
    t = Test()
    t.Hello()
