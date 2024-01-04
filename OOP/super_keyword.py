# super() keyword in python
class Student:
    def __init__(self, name, roll, year, branch):
        self.name = name
        self.roll = roll
        self.year = year
        self.branch = branch

    def display(self):
        print("Name: ", self.name)
        print("Roll: ", self.roll)
        print("Year: ", self.year)
        print("Branch: ", self.branch)


# Single Inheritance

class CR(Student):
    def __init__(self, name, roll, year, branch, position):
        super().__init__(name, roll, year, branch)
        self.position = position

    def display(self):
        super().display()
        print(f"Position : {self.position}")


# Creating objects
s2 = Student("Sunil", 3469, 2021, "CSE")
s2.display()

s1 = CR("Suraj", 3469, 2021, "CSE", "CR")
s1.display()


# print(dir(s1))
