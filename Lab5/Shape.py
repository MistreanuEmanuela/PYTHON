import math


class Shape:
    def __init__(self, nr_sides):
        if nr_sides >= 0:
            self.sides = nr_sides
        else:
            raise Exception("You can't have a negative number of sides")

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius > 0:
            super().__init__(0)
            self.radius = radius
        else:
            raise Exception("Radius should be a positive number")

    def get_radius(self):
        x = self.radius
        return x

    def area(self):
        area = (self.radius ** 2) * math.pi
        return area

    def perimeter(self):
        perimeter = self.radius * 2 * math.pi
        return perimeter


class Rectangle(Shape):
    def __init__(self, width, length):
        if width > 0 and length > 0:
            super().__init__(4)
            self.width = width
            self.length = length
        else:
            raise Exception("Width and length should be positive numbers")

    def get_width(self):
        x = self.width
        return x

    def get_length(self):
        x = self.length
        return x

    def area(self):
        area = self.length * self.width
        return area

    def perimeter(self):
        perimeter = (self.length + self.width)*2
        return perimeter


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__(3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_side(self):
        x = (self.side1, self.side2, self.side3)
        return x

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        area = (p * (p - self.side1) * (p - self.side2)*(p - self.side3)) * (1/2)
        return area

    def perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter


circle = Circle(5)
print("Radius:", circle.get_radius())
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())

triangle = Triangle(3, 4, 5)
print("Triangle:", triangle.get_side())
print("Area:", triangle.area())
print("Perimeter:", triangle.perimeter())

rectangle = Rectangle(5, 6)
print("Reactangle: ", rectangle.get_length(), " ", rectangle.get_width())
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())