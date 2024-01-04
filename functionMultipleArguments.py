# Program to show the use of Multiple arguments in function
# using      *args
def add(*nums):
    total = 0
    for i in nums:
        total += i
    return total


print("3 + 5 + 2              =", add(3, 5, 2))
print("1 + 2 + 3 + 4 + 5      =", add(1, 2, 3, 4, 5))
print("1 + 2 + 3 + 4 + 5 + 10 =", add(1, 2, 3, 4, 5, 10))


# passing structure like dictionary
# using    **kwargs
def fruits_total(**fruits):
    total = 0
    for i in fruits.values():
        total += i
    return total


print("Total Fruits units = ", fruits_total(apple=2, banana=5))
print("Total Fruits units = ", fruits_total(apple=2, banana=5, oranges=10))
print("Total Fruits units = ", fruits_total(
    apple=2, banana=5, oranges=10, grapes=25))
