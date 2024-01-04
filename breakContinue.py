name = input("Enter Your Name : ")

for ch in name:
    if ch == 'a':
        break
    print(ch)

print()
print()
for i in range(10):
    if i == 6:
        print("Skipped")
        continue
    print(i)
    i = i+1
