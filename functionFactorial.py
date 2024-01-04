# Functions in Python
# Python program to find Factorial of user input number
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)


num = int(input("Enter any Number : "))

fact = factorial(num)
print("Factorial of", num, "is", fact)
