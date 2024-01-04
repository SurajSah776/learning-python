# Introduction to classes and objects

class Student:
    # name = "Suraj Kumar Sah"
    # roll = 21053469
    # year = "Third"

    # Using Constructors
    def __init__(self, name, roll, year):
        self.name = name
        self.roll = roll
        self.year = year

    def show(self):
        print(
            f"I am {self.name} having roll number {self.roll} and currently studying in {self.year} year in KIIT University")


# Creating object
# stud1 = Student()
# stud1.show()
# print(stud1.name)
# print(stud1.roll)
# print(stud1.year)


# Creating object with constructors
stud2 = Student("Suraj", 3469, "Third")
stud2.show()
