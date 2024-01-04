# Types of access modifiers in python OOP
#  Public Access Modifiers
#  Private Access Modifiers
#  Protected Access Modifiers

class Student:
    def __init__(self, name, roll, section):
        self.__name = name  # Private
        self._roll = roll  # Protected
        self.section = section  # Public

    def display(self):
        print(f"Name    : {self.__name}")
        print(f"Roll    : {self._roll}")
        print(f"Section : {self.section}\n")


# creating objects
stud1 = Student("Suraj", 3469, "CSE-09")
# Student.display(stud1)
stud1.display()

stud2 = Student("Sunil", 2954, "CSE-09")
stud2.display()

print(stud1._Student__name)  # Accessing Private Variable   ( Name Mangling )
print(stud1._roll)  # Accessing Protected Variable
print(stud1.section)  # Accessing Public Variable
