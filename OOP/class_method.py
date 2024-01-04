# Class Methods in python

class Number:
    count = 0

    def __init__(self):
        print("Constructor Called")

    @classmethod
    def sum(cls, a, b):
        cls.count += 1
        print("This is Class Method")
        return a+b


# Creating Object
num1 = Number()
num2 = Number()
print("Sum = ", num1.sum(2, 5))

num1.count = 8
print(num1.count)

print(num2.count)

print(f"count Value = {Number.count}")
