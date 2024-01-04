# List in python
# Creating list with List constructor list(())
new_list = list(("Suraj", "Kumar", "Sah", 3, 4, 6, 9))
print(new_list)


print(new_list[0])
print(new_list[-4])
print(new_list[3:-2])

if 'Suraj' in new_list:
    print("Yes")
else:
    print("No")

# List Comprehension
print()
print("List Comprehension".center(35))
new = [item for item in new_list]
print(new)

# List Methods
print()
print("List Methods".center(30))

var = [2, 6, 0, -1, -8, 9, 2, 10, 15]
print(var)

var.sort()  # Sort
print(var)

var.sort(reverse=True)
print(var)

var.reverse()  # Reverse
print(var)

var.append(3468)  # Append
print(var)

print(var.index(9))  # Index

print(var.count(2))  # count

# Copying a List from another list
new_l = var.copy()
print("Original List : ", var)
print("Copied List   : ", new_l)

var.insert(5, 21053459)  # Insert into specified location index
print(var)

var.extend(new_list)  # Extend
print(var)

# Concatenation of two Lists
print()
print("Concatenation of two Lists".center(35))
var1 = [1, 2, 3, 4, 5, 6]
var2 = [-1, -2, -3, -4]

varNew = var1+var2
print(varNew)

# Clear
var1.clear()
print(var1)

# pop
print(var2)
var2.pop()
print(var2)
var2.pop(0)
print(var2)

# remove
print(var)
var.remove("Kumar")
print(var)

# List Repetition
print()
print("List Repetition".center(35))
print(var2*3)
