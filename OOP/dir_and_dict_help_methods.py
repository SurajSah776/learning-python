# dir(), __dict__ and help() in python

# dir()
marks = [98, 80, 75, 34]
x = 6

# print(dir(marks))
print()
print()

# print(dir(x))

print()
print()


# help()
# print(help(marks))

print()
print()

# print(help(x))


print()
print()


# __dict__ attribute

class Student:
    def __init__(self, name, roll, year, branch):
        self.name = name
        self.roll = roll
        self.year = year
        self.branch = branch
        self.cgpa = 9.3
        self.behaviour = 'Excellent'


stud = Student("Suraj", 3469, 2021, "CSE")
print(stud.__dict__)
