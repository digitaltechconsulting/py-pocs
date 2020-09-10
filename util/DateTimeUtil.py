import datetime 
class DateTimeUtil:
    @staticmethod
    def GetUtcTimeStamp():
        timestamp = str(datetime.datetime.now() )
        return timestamp

    
if __name__ == "__main__":
    utcTimeStamp = DateTimeUtil.GetUtcTimeStamp()
    print(utcTimeStamp)