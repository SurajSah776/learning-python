# Decorators in python

def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()


'''
def greet(func):
    def decorated_func():
        print("Hello")
        func()
        print("Goodbye")
    return decorated_func()


print()

@greet
def sum():
    print("Sum Function Called")

print()
'''
