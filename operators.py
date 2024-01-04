# We will see different operators used in python

# and operator
a = 10
b = 6
print()
print("*** Arithmetic Operators ***".center(35))
print("Addition =", a+b)
print("Subtraction =", a-b)
print("Division =", a/b)
print("Modulus =", a % b)
print("Multiplication =", a * b)
print("Floor Division =", a // b)
print("Exponent =", a ** b)
print()

print("*** Comparison Operators ***".center(35))
print("5==5 :", 5 == 5)
print("5!=5 :", 5 != 5)
print("5<=5 :", 5 <= 5)
print("5>=5 :", 5 >= 5)
print("5> 5 :", 5 > 5)
print("5< 5 :", 5 < 5)
print()

print("*** Logical Operators ***".center(35))
print("6==5 and 5!=4 :", 6 == 5 and 5 != 4)
print("6==5 or 5!=4  :", 6 == 5 or 5 != 4)
print("not 5==4      :", not 5 == 4)

print()

print("*** Assignment Operators ***".center(35))
a, b = 5, 3
c = a
print("Initially, a =", a, "b =", b)
print("c = a  :", c)
c += b
print("c += b :", c)
c -= b
print("c -= b :", c)
c /= b
print("c /= b :", c)
c *= b
print("c *= b :", c)
c %= b
print("c %= b :", c)
c //= b
print("c //= b :", c)
c **= b
print("c **= b :", c)

print()

print("*** Bitwise Operators ***".center(35))
a, b = 10, 15
print("Decimal, a =", a)
print("Binary,  a =", bin(a), "b =", bin(b))
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a    =", ~a)
print("a << 2 =", a << 2)
print("b >> 2 =", b >> 2)


print()
print("*** Membership Operators ***".center(35))
print("'a' in 'Suraj' :", 'a' in 'Suraj')
print("'a' not in 'Suraj' :", 'a' not in 'Suraj')

print()

print("*** Identity Operators ***".center(35))
print("'Suraj' is 'Suraj' :", 'Suraj' is 'Suraj')
print("'Suraj' is not 'Suraj' :", 'Suraj' is not 'Suraj')

print()
