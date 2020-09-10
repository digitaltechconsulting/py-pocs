class Dog:
    def __init__(self):
        self.name = "Hemant"
        self.lastName = "Shelar"
    def Print(self):
        print('my name is {name} {lastName}'.format(name=self.name,lastName=self.lastName))

x = Dog();
x.Print()