# Set in python

print()
print("*** Creating Sets ***".center(25))
marks = {2, 1, 0, 5, 3, 4, 6, 9}  # Using curly braces {}
print(type((marks)))
print(marks)

var = set()  # Using set() method
print(type(var))

print()


print()
print("*** Adding items to the Set ***".center(25))

print(marks)
marks.add(100)  # Adding single item using add() method
print("After Adding 100 : ", marks)

# Adding multiple items using update() method
marks.update([100, 200, 300])
print("After Adding 100, 200 and 300 : ", marks)

print()


print()
print("*** Removing items from the Set ***".center(25))

print(marks)
marks.discard(100)  # Removing 100 using discard() method
print("After removing 100 : ", marks)

# Removing an element using remove() method

marks.remove(200)
print("After Removing 200 : ", marks)
# marks.remove(200)
# print("After Removing 200 : ", marks) #Gives Error when 200 is not in the set

print()


print()
print("*** Set Operations ***".center(25))
set1 = {1, 2, 4, 5, 6, 7, 9, 10}
set2 = {2, 4, 6, 8, 10}

# Union
print("Union : ", set1 | set2)
print("Union : ", set1.union(set2))
print()

# Intersection
print("Intersection : ", set1 & set2)
print("Intersection : ", set1.intersection(set2))
print()

# Difference
print("Difference : ", set1 - set2)
print("Difference : ", set1.difference(set2))
print()

# Symmetric Difference (A - B) U (B - A)  or  (A U B) - (A n B)
# print(set1, set2)
print("Symmetric Difference : ", set1 ^ set2)
print()


print()
# Set comparisons (>, <, <=, >=, ==)
print("*** Set Comparisons ***".center(30))
A = {1, 2, 3, 47, 90, 56}
B = {2, 4, 7, 3, 56}
print("A = ", A)
print("B = ", B)
print()
print("A > B  : ", A > B)
print("B > A  : ", B > A)
print("A < B  : ", A < B)
print("B < A  : ", B < A)
print("A == B : ", A == B)
print()
print("*** Set Methods ***".center(30))
A = {2, 3, 4}
B = {1, 3, 4, 2, 6}
print("A = ", A)
print("B = ", B)
print("A.isdisjoint(B) : ", A.isdisjoint(B))
print("A.issuperset(B) : ", A.issuperset(B))
print("B.issuperset(A) : ", B.issuperset(A))
print("A.issubset(B) : ", A.issubset(B))
print("B.issubset(A) : ", B.issubset(A))


print()
print()
print("set1 =", set1)
print("set2 =", set2)
set1.intersection_update(set2)
print("set1.intersection_update(set2) : ", set1)

# set1.difference_update(set2)
# print("Difference_Update : ", set1)

print()
