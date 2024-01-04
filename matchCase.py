num = int(input("Enter day Number : "))

match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day Number")

name = input("Enter Your Name : ")
count = 0
for ch in name:
    match ch:
        case 'S':
            print("S")
        case 'u':
            print("u")
        case 'r':
            print("r")
        case 'a':
            print("a")
        case 'j':
            print("j")
        case _:
            count = count+1
print(count, " letters not Found")
