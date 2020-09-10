import inspect
import pika
import sys
sys.path.insert(0,'..')
from logger.log import *


class RMQManager:
    def __new__(self):
        funcName = inspect.currentframe().f_code.co_name
        self.logger = Logger();
        self.logger.LogInfo(funcName)
        self.connection = pika.BlockingConnection('localhost')
        
    def __init__(self):
        print("I am in __init__.")
        self.test = 1
    def SendMessage(self):
        channel = self.connection.channel();
        channel.basic_publish()
        
        



if __name__ == "__main__":
    print("I am in inside RMQManager")
    r = RMQManager()
    
