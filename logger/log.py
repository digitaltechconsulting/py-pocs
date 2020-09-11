import time
import sys
sys.path.insert(0,'..')
from util.DateTimeUtil import *
class Logger:
    def LogInfo(self,message):
        timeStamp = DateTimeUtil.GetUtcTimeStamp()
        print('{timeStamp} : {message}'.format(message=message,timeStamp=timeStamp))
    def LogWarning(self, message):
        print(message);
    def LogError(self,message):
        print(message)
        


if __name__ == "__main__":
    logger = Logger()
    logger.LogInfo("This is test info message")
    logger.LogWarning("This is test warning message")
    logger.LogError("This is test error message")