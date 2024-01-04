# Generators in Python

def my_generator():
    for i in range(500):
        yield i


# Using the Generator Function
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


for i in gen:
    print(i)
