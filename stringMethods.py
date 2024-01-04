str1 = 'Suraj Kumar Sah'
str2 = "sunil Prasad Yadav"

# Methods in strings
# Length
print(len(str1))
print(str1[:5])

print()
print(str1[6:-4])

print()
print(str1[-6:-4])

# Upper and Lower case
print("upper() :", str1.upper())
print("lower() :", str1.lower())


str1 = "!!!Suraj Kumar !!! Sah !!!!"
print(str1)
print("rstrip() :", str1.rstrip("!"))
print("rstrip() :", str1.lstrip("!"))

print()
print("replace() :", str1.replace("!!!", "."))

print()
print("split() :", str1.split())  # makes list after splitting

print()
print("capitalize() :", str2.capitalize())

print()
print("center() :", str2.center(50))
# print(len(str2.center(50)))

print()
print("count() :", str1.count("!"))

print()
print("Sunil Prasad Yadav ends with Yadav : ", str2.endswith("Yadav"))

print()
print(str2.endswith("Prasad", 6, 12))

print()
print("sunil Prasad Yadav starts with Sunil : ", str2.startswith("sunil"))

print()
print("'Suraj' is present in str1 at starting index ",
      str1.find("Suraj"))  # else return -1

print()
# print("'Suraj' is present in str1 at starting index ", str1.index("suraj"))  # else return exception


str = "suraj1 sah"
print()
# checks entire string is alphanumeric or not.
print("isalnum() : ", str.isalnum())

print()
# checks entire string is only alphabet or not.
print("isalpha() : ", str.isalpha())


print()
# Checks if all characters are in lowercase
print("islower() : ", str.islower())

print()
# Checks if all characters are in uppercase
print("isupper() : ", str.isupper())

print()
# Checks if all characters are printable
print("isprintable() : ", str.isprintable())

print()
# Checks if there is space
st = " "
print("isspace() : ", st.isspace())


print()
stt = "Suraj"
# Checks if only first letter is capitalized
print("istitle() : ", stt.istitle())

print()
# swaps all the uppercase to lowercase and vice-versa
print("swapcase() : ", str2.swapcase())

print()
stt = "My name is suraj kumar sah"
# capitalize first letter of each word in a string
print("title() : ", stt.title())


print(list(range(2, 10, 1)))
