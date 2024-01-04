# Operator Overloading

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def display(self):
        return (f"{self.i}i + {self.j}j + {self.k}k")

    def __add__(self, obj):
        return f"{self.i+obj.i}i + {self.j+obj.j}j + {self.k+obj.k}k"

    def __mul__(self, obj):
        return f"{self.i*obj.i}i + {self.j*obj.j}j + {self.k*obj.k}k"


# Creating Objects


v1 = Vector(9, 2, 3)
v2 = Vector(4, 5, 6)

print(f"V1 =", v1.display())
print(f"V2 =", v2.display())

print(f"Sum =", (v1+v2))
print(f"Mul =", (v1*v2))
