# Walrus Operator [:=] (Addition in Python 3.8 onwards)
a = True
print(a := False)

num = [3, 4, 6, 9]
while (n := len(num) > 0):
    print(num.pop())


food = list()

while (f := input("Enter your favourite food (quit-to end): ") != "quit"):
    food.append(f)

print(food)
