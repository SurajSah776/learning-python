# Dunder or Magic methods ( Starting and Ending with double underscore __ )

# from classes import Student

# s1 = Student("Suraj", 3469, 2021)
# s1.show()

class Student:
    def __init__(self, name, roll, year):
        self.name = name
        self.roll = roll
        self.year = year

    def show(self):
        print(
            f"I am {self.name} having roll number {self.roll} and currently studying in {self.year} year in KIIT University")

    #  __str__
    def __str__(self):
        return f"Name of student : {self.name},   roll : {self.roll}   and   year of passing : {self.year}"

    #  __repr__
    def __repr__(self):
        return f"Student('{self.name}', {self.roll}, {self.year})"

    #  __call__
    def __call__(self):
        print("__call__ method is called")


# Creating Object
s1 = Student("Suraj", 3469, 2021)
# s1.show()

print(s1)
# print(str(s1))
# print(repr(s1))


# __call__ method (making object callable)
s1()
