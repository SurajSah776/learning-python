import time
print()
print("Current System Time is", time.strftime('%H:%M:%S'))
print()

hr = int(time.strftime('%H'))
# print("Hours :", hr)
min = int(time.strftime('%M'))
# print("Minutes :", min)
sec = int(time.strftime('%S'))

if (hr < 12 and min <= 59 and sec <= 59):
    print("Good Morning Sir")

elif (hr >= 12 and hr < 16 and min <= 59 and sec <= 59):
    print("Good Afternoon Sir")

elif (hr >= 17 and hr < 18 and min <= 59 and sec <= 59):
    print("Good Evening Sir")
else:
    print("Good Night Sir")

print("Thank You")
print()
