# Local variable and Global variable

x = 10


def func():
    # x = 5  # local Variable
    global x  # Global x
    x = 8
    print(f"Value of x is {x}")


func()
