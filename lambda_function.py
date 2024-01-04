# *** Lambda Function ***

# Lambda functions are small anonymous functions.
# They are created by using the keyword lambda.

# To add three numbers

# def sum(a, b, c):  # Normal Function
#     return a+b+c


def sum(a, b, c): return (a+b+c)
# sum = lambda a, b, c: a + b + c


print("Sum =", sum(5, 6, 2))


# passing function as argument in lambda function

def apply(square, value):
    return square(value)


def square(val):
    return val**2


print("Square of 2 =", square(2))
print("Square of 2 =", apply(square, 2))

# Other Example
x = 5
y = 10
# a =lambda x, y: print(f"{x} * {y} = {x*y}")
def a(x, y): return print(f"{x} * {y} = {x*y}")


print("Multiplication : ", a(x, y))
