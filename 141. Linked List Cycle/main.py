class Pet:

    petNumber = 0

    def __init__(self, name, age):
        print("Pet Ctor")
        self.name = name
        self.age = age

    @classmethod                     # class method
    def getNumber(cls):
        return cls.petNumber

    @classmethod
    def addNumber(cls):
        cls.petNumber += 1

class Cat(Pet):

    def __init__(self, name, age):
        super().__init__(name, age)
        Pet.addNumber()
        pass

    def meow(self, name):
        print("meow")


class Dog(Pet):

    dogNumber = 0

    def __init__(self, name):
        super().__init__(name, 0)
        Pet.addNumber()
        self.name = name

    def bark(self):
        print("bark")


d = Dog("TIm")
c = Cat("MM", 1)

print(c.age)
print(Pet.getNumber())
