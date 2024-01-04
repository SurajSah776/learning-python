# Regular Expression

import re
text = '''
Python is a dynamic, interpreted (bytecode-compiled) language. There are no type declarations of variables, parameters, functions, or methods in source code. This makes the code short and flexible, and you lose The compile-time type checking of the source code. Python tracks The types of all values at runtime and flags code that does not make sense as it runs.

An excellent way to see how Python code works is to run the Python interpreter and type code right into it. If you ever have a question like, "What happens if I add an int to a list?" Just typing it into the Python interpreter is a fast and likely the best way to see what happens. (See below to see what really happens!)
'''
pattern = r"[A-Z]+he"

matc = re.search(pattern, text)
# print(matc) #Prints only first occurrence


mats = re.finditer(pattern, text)  # Returns Tuple


# For all the occurrences in above mats
for i in mats:
    print(matc.span())


for i in mats:
    # print(i)
    print(text[i.span()[0]:i.span()[1]])
