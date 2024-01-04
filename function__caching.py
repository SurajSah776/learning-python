# Function Caching in python


# from functools import lru_cache
import functools
import time
# Function for Fibonacci Series


# @functools.lru_cache(maxsize=None)
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)


# print(fib(20))


@functools.lru_cache(maxsize=None)
def funMul(num):
    time.sleep(4)
    return num*2


print(funMul(5))
print("Done for 6")

print(funMul(6))
print("Done for 6")

print(funMul(10))
print("Done for 10")

print(funMul(6))
print("Done for 6")
print(funMul(5))
