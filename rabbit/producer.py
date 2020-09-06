import Logger as l
import pika
import config

c = config.AppSettings()

def StartProducer():
    
    print(c.rabbitServer)
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel();
    
    channel.queue_declare(queue=c.queue)
    

if __name__ == "__main__":
    l.LogMessage("running producer.py directly")
    StartProducer()
    
    