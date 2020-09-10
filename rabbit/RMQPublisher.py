import inspect
import pika
import sys
sys.path.insert(0,'..')
from logger.log import *


class RMQPublisher:
    def __init__(self,host):
        funcName = inspect.currentframe().f_code.co_name
        self.logger = Logger()
        self.logger.LogInfo(funcName)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.exchange = 'motion-detected'
        self.routingKey = 'known.motion'

    def PublishMessage(self):
        channel = self.connection.channel()
        body = '{"id":"1","name":"Hemant"}'
        channel.basic_publish(self.exchange,
        self.routingKey,body)
        channel.close()

    def Close(self):
        self.connection.close()

if __name__ == "__main__":
    print("I am in inside RMQManager")
    r = RMQPublisher(host="192.168.1.115")
    r.SendMessage()
    r.Close()
    
