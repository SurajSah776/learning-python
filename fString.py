print()
print("Old String Formatting in Python".center(50))

print()
print("1. Using % - formatting".center(30))
str1 = 'Suraj'
str2 = 'Sah'
age = 22
print("Hello %s %s, are you %s years old?" % (str1, str2, age))

print()
print("2. str.format()".center(22))
print("Hello {} {}, are you {} years old?".format(str1, str2, age))


print()
str3 = 'Hello {} {}, are you {} years old?'
print(str3.format(str1, str2, age))
print()
# These both methods are not recommended more in modern programming.

# so F Strings are used from python 3.6 onwards
print()
print("***** Using f strings *****".center(30))

name = 'Suraj Sah'
roll = 21053469
age = 22
print(f"My name is {name} and I am {age} years old having roll number {roll}")
print()
