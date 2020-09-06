class RMQManager:
    def __new__(self):
        print("I am in __new__")
    def __init__(self):
        print("I am in __init__.")
        self.test = 1
        



if __name__ == "__main__":
    print("I am in inside RMQManager")
    r = RMQManager()
    print(r.test)