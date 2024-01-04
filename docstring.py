# In this program, we are going to see the use of docstring
# Docstring is not same as Comments (Comments do not affect the output of the program but docstring may do)
# doctring can be printed but comments can't be printed
# It's placed just beneath/below the function, module, or class to explain what they perform.
# The docstring is then readily accessible in Python using the __doc__ attribute.

name = 'Suraj Kumar Sah'
age = 22


def add(n1, n2):
    '''This Function takes 2 numbers as arguments and add them'''
    print("Sum =", (n1+n2))


# Calling the function
add(10, 20)

# To print the docstring
print(add.__doc__)
