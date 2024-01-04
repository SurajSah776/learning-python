str1 = 'Suraj Kumar Sah'
str2 = "Sunil Prasad Yadav"
str3 = """Shristi Dutta"""
str4 = '''Sanjay Sah'''
str5 = """Anuj
Kumar
Prajapati"""

str6 = '''Anuj
Kumar
Prajapati'''

str7 = 'Anuj Kumar Prajapati'

print()
print("Hello " + str3)  # Concatenation


print("\nPrinting all the Strings\n", str1, "\n", str2, "\n", str3, "\n",
      str4, "\n", str5, "\n", str6, "\n", str7)
print()

print(str5 == str6)  # True
print()

print(str1[0])
print()

print(str1[1:5])
print()

for char in str3:
    print(char)
