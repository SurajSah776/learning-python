# Importing reduce from functools to use reduce()
from functools import reduce

# map()
# Syntax : map(function, iterable)
# iterable may be list, dictionary, etc


def cube(num):
    return num**3


roll = [2, 1, 0, 5, 3, 4, 6, 9]
newRoll = list(map(cube, roll))

print("Cube : ", newRoll)

# filter()
# Syntax : filter(function, iterable)


def is_even(num):
    return num % 2 == 0


even = list(filter(is_even, roll))
print("Only even numbers filtered :", even)

# reduce()
# Syntax : reduce(function, iterable)
# we must import reduce from functools

num = [1, 2, 3, 4, 5]


def add(x, y):
    return x + y


afterAdd = reduce(add, num)
print("Reduce : ", afterAdd)
