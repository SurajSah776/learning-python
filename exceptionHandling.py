# Exception Handling in Python

# Python code to catch an exception and handle it using try and except code blocks

a = ["Python", "Exceptions", "try and except"]
try:
    # looping through the elements of the array a, choosing a range that goes beyond the length of the array
    for i in range(4):
        print("The index and element from the array is", i, a[i])
except:
    print("Index out of range")


print()
print()
print()


# Python program to show how to use else clause with try and except clauses

# Defining a function which returns reciprocal of a number
def reciprocal(num1):
    try:
        reci = 1 / num1
    except ZeroDivisionError:
        print("We cannot divide by zero")
    else:
        print(reci)


# Calling the function and passing values
reciprocal(4)
reciprocal(0)


print()
print()
print()


# Python program to show how to use assert keyword
def square_root(Number):
    assert (Number < 0), "Give a positive integer"
    return Number**(1/2)


print(square_root(36))
print(square_root(-36))

print()
print()
print()

# Python code to show how to raise an exception in Python
num = [3, 4, 5, 7]
if len(num) > 3:
    raise Exception(
        f"Length of the given list must be less than or equal to 3 but is {len(num)}")


print()
print()
print()


# a = int(input("Enter number between 5 and 9 : "))

# if (a < 5 or a > 9 or a != 'quit'):
#     raise ValueError("Value Error Occurred")
