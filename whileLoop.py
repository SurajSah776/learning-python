name = input("Enter Your Name : ")
i = 1
while i < 3:
    print(name)
    i = i+1
    for ch in name:
        print(ch)

else:
    print("Else part of While Loop")

# Do While Loop emulating
i = 0
while True:
    print(i)
    i = i+1
    if (i == 5):
        print("Break Statement Executed")
        break
