# Static method in python

class Employee:
    noOfEmp = 0

    def __init__(self, name, empID, experience):
        self.name = name  # Instance Variable
        self.empID = empID
        self.experience = experience
        # No Of Employees
        Employee.noOfEmp += 1  # Class Variable

    def display(self):
        print(f"Name of Emp : {self.name}")
        print(f"Employee ID : {self.empID}")
        print(f"Experience  : {self.experience}\n")

    @staticmethod
    def displayInfo():
        print("This is static method")


# Creating Object
emp1 = Employee("Suraj", 100, 1)
emp1.display()

emp2 = Employee("Sunil", 101, 2)
emp2.display()

Employee.displayInfo()  # Calling the static method

print(f"Total No. of Employees = {Employee.noOfEmp}")


emp1.noOfEmp = 4  # This will act like an instance variable here
emp2.noOfEmp = 8  # This will act like an instance variable here

Employee.noOfEmp = 10  # Changing the Class Variable

print(emp1.noOfEmp)
print(emp2.noOfEmp)

print(Employee.noOfEmp)
