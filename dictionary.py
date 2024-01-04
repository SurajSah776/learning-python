# Dictionary in Python
'''
   * Python Dictionary is used to store the data in a key-value pair format.
   * dict = {key1:value1, key2:value2, ...}
   * It is the mutable data-structure.
   * Accessing through key : dict["key1"]
   * It is fast as element can be accessed with key
'''
print()
# Creating a Dictionary
print("*** Creating a Dictionary ***".center(40))
# 1.
Dict = {'name': 'Suraj', 'roll': 3469, 'contact': 1234567890}
# print(type(Dict))
print(Dict)

# 2.
Dict = dict({'name': 'Suraj', 'roll': 3469, 'contact': 1234567890})
print(Dict)

# 3.
Dict = dict([('name', 'Suraj'), ('roll', 3469), ('contact', 1234567890)])
print(Dict)

print()
print()

print("*** Accessing Dictionary values***".center(40))
print("Single value =  Dict['name'] :", Dict['name'])
print("Single value =  Dict.get('name') :", Dict.get('name'))
print()
print("Multiple value")
print("Dict.keys() : ", Dict.keys())
print("Dict.values() : ", Dict.values())
print("Dict.items() : ", Dict.items())


print()
print()

print("*** Iterating In Dictionary ***".center(40))
print("Printing only Keys")
for k in Dict:
    print(k)

print()
print("Printing only Values")

print()
print("Printing Both Keys and Values using items() method")
for k, val in Dict.items():
    print("Keys  Values  : ", k, val)


print()
print()

print("*** Dictionary Methods ***".center(40))

d1 = {'name': 'Suraj', 'roll': 3469, 'contact': 7890}
d2 = {'programme': 'B.Tech', 'course': 'CSE'}

# Adding item to Dictionary
print("Before Adding  : ", d1)
d1['age'] = 22
print("After Adding   : ", d1)
print()

d1.pop('age')
print("After Popping, d1.pop('age')  : ", d1)
print()

print("Before Popping              :", d1)
d1.popitem()
print("After Popping, d1.popitem() :", d1)
print()

print("Length of Dict : len(Dict) : ", len(Dict))
print("Length of d2 : len(d2)     : ", len(d2))

print()
print()

new = d1.copy()
print("copy() : new = d1.copy() : ", new)
print("Before d1.clear() :", d1)
d1.clear()
print("After d1.clear()  :", d1)

print()
print()
