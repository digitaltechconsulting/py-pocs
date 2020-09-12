class Test:
    def __init__(self):
        print("Inside init")
        self.name = "123456789"
        self.list = [1,2,3,4,5,6,7,8,9]
        self.tuple = (1,2,3,4,5,6,7,8,9)
    def __del__(self):
        print("Inside destrouctor")
    def Test(self):
        lastNumber = self.list[-1] 
        print(lastNumber)
        reverseList = self.list[::-1]
        print(reverseList)
    def student(self,name,age,**marks):
        print(name)
        print(age)
        print(marks['maths'])

if __name__ == "__main__":
    t = Test()
    t.Test()
    t.student("Hemant",40,maths=60,bio=20)
