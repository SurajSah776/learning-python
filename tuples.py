# Tuples in Python
tup = tuple((1, 2, 54, 5, 435, 9))  # Using Tuple constructor tuple(())
print(tup)

tupl = (2, 9, 0, 12, 48, -1)
print(tupl)

print(tupl[4])
print(tupl[:4])
print(tupl.index(12))
print(tupl.index(0, 1, 4))

# Concatenating two tuples
tup1 = (1, 2, 8, 0)
tup2 = ('S', 5, 'Sah', 8, 9)
tup3 = tup1 + tup2
print(tup3)


# Manipulating Tuples (indirectly)
print()
print("Manipulating Tuples (indirectly)".center(45))
tup = ('Suraj', 'Sunil', 'Ram', 'Aryan', 'Paro')
temp = list(tup)
print(temp)

temp.append('Anuj')
temp.pop(4)
temp[3] = 'Jaan'
tup = tuple(temp)
print(tup)
