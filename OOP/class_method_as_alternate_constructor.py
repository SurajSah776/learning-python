# Using class method as Alternate Constructor

class Student:
    def __init__(self, name, roll, year, branch):
        self.name = name
        self.roll = roll
        self.year = year
        self.branch = branch

    def display(self):
        print(
            f"Name: {self.name}\nRoll: {self.roll}\nYear: {self.year}\nBranch: {self.branch}")

    # Alternate Constructor using class method

    @classmethod
    def fromStringToData(cls, string):
        # name, roll, year, branch = string.split('-')
        name = string.split('-')[0]
        roll = string.split('-')[1]
        year = string.split('-')[2]
        branch = string.split('-')[3]
        return cls(name, roll, year, branch)


# Creating objects

# stud1 = Student('Suraj Kumar Sah', 3469, 2021, 'CSE')
# stud1.display()
inputData = "Sunil Prasad Yadav-2954-2021-CSE"

# Using alternate constructor
stud2 = Student.fromStringToData(inputData)
stud2.display()
