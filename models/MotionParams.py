import uuid
import sys
sys.path.insert(0,'..')
from util.DateTimeUtil import *

class MotionParams:
    def __init__(self):
        self.when = DateTimeUtil.GetUtcTimeStamp()
        self.name = "test"
        self.id = uuid.uuid4().hex
    def Show(self):
        pass

if __name__ == "__main__":
    mp = MotionParams()
    mp.Show()
    json = mp.__dict__
    print(json)
