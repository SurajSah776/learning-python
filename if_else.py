mark = int(input("Enter Your Marks in COA :"))
age = input("Enter your age : ")
print("age = ", age)

if (mark > 100 or mark < 0):
    print("Invalid Mark")
elif (mark >= 90):
    print("Grade : O")
    if (mark >= 90 and mark <= 100):
        print("Outstanding")
elif (mark >= 80):
    print("Grade : E")
    if (mark >= 80 and mark < 90):
        print("Excellent")
elif (mark >= 70):
    print("Grade : A")
elif (mark >= 60):
    print("Grade : B")
elif (mark >= 50):
    print("Grade : C")
elif (mark >= 40):
    print("Grade : D")
else:
    print("Grade : F")
