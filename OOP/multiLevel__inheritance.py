# Multi-Level inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name   :", self.name)


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display(self):
        super().display()
        print("Breed  :", self.breed)


class GoldenDog(Dog):
    def __init__(self, name, breed, color):
        super().__init__(name, breed)
        self.color = color

    def display(self):
        super().display()
        print("Color  :", self.color)


# Creating Object
dog = GoldenDog("My Love", "German", "Golden")
dog.display()
