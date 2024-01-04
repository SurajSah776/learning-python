# 'is' vs '==' in python
# is is used to compare the object identity
# == is used to compare the object value


print("*** Checking on numbers and strings ***".center(30))
a = 5
b = "5"
c = 5
print(a is b)
print(a == b)

print()

print(a is c)
print(a == c)


#  Checking on list
print()
print("*** Checking on list ***".center(20))
l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]

print(l1 is l2)
print(l1 == l2)

#  Checking on Set
print()
print("*** Checking on Set ***".center(20))

s1 = {2, 1, 4, 3}
s2 = {1, 2, 3, 4}

print(s1 is s2)
print(s1 == s2)


#  Checking on dictionary
print()
print("*** Checking on Dictionary ***".center(20))

d1 = {"n1": 1, "n2": 2}
d2 = {"n1": 1, "n2": 2}


print(d1 is d2)
print(d1 == d2)
