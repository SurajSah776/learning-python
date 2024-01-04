# Method Overriding

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2*(self.length + self.breadth)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def area(self):  # Overriding
        return self.length * self.length

    def perimeter(self):  # Overriding
        return 4 * self.length


# Creating Object

rect = Rectangle(3, 5)
print("Area = ", rect.area())
print("Perimeter = ", rect.perimeter())


sq = Square(5)
print("Area = ", sq.area())
print("Perimeter = ", sq.perimeter())
