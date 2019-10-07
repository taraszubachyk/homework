class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = self.name + "s age is " + str(self.age)

    def getInfo(self):
        print(self.info)


p1 =Person("Jonh", 25)
p1.getInfo()

