
import math
from parent import Shape

# base abstract class


class Rectangle(Shape):
    sides = 4

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def printarea(self):
        print("Area is:", self.length * self.breadth)

    def printperimeter(self):
        print("Perimeter is:", 2 * (self.length + self.breadth))

    def get_sides(self):
        print("Number of sides are:", self.sides)


# regPolygon is inherited from Shape
# Polymorphism is shown by printarea, printperimeter an get_sides function

class regPolygon(Shape):
    def __init__(self, nsides=3, side=4):
        self.n = nsides
        self.l = side

    def printarea(self, name):
        p = self.l * self.n
        a = p/math.tan(180/self.n)
        A = p * a
        print(f"Area of {name} is: ", A/2)

    def printperimeter(self, name):
        print(f"Perimeter of {name} is: ", self.n * self.l)

    def get_sides(self, name):
        print(f"Number of sides in a {name} are: ", self.n)


# Square is inherited from regPolygon
class Square(regPolygon):
    def diagonal(self):
        print("Length of diagonal is: ", math.sqrt(2) * self.l)


class Pentagon(regPolygon):
    def no_diagonal(self):
        print("Number of diagonal is: ", self.n*(self.n - 3) % 2)


class Hexagon(regPolygon):
    def no_diagonal(self):
        print("Number of diagonal is: ", self.n*(self.n - 3) % 2)


class Rhombus(Shape):
    sides = 4

    def __init__(self, height, base):
        self.h = height
        self.b = base

    def printarea(self):
        print("Area of rhombus is: ", self.b * self.h)

    def printperimeter(self):
        print("Perimeter of rhombus is: ", self.b * 4)

    def get_sides(self):
        print("Number of sides in a rhombus are:", self.sides)


class Trapezoid(Shape):
    sides = 4

    def __init__(self, height, base, s, c, d):
        self.h = height
        self.b = base
        self.s = s
        self.c = c
        self.d = d

    def printarea(self):
        print("Area of trapezoid is: ", (self.b + self.s) * self.h / 2)

    def printperimeter(self):
        print("Perimeter of trapezoid is: ",
              self.c + self.s + self.b + self.d)

    def get_sides(self):
        print("Number of sides in a trapezoid are:", self.sides)


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def circumference(self):
        return 2 * math.pi * (self.radius)


class Ellipse(Circle):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return math.pi * (self.a) * (self.b)

    def circumference(self):
        return math.pi * ((self.a) + self.b)


class Sphere(Circle):
    def surface_area(self):
        return 4 * super().area()


if __name__ == "__main__":

    r1 = Rectangle(40, 80)
    r1.printarea()
    r1.printperimeter()
    r1.get_sides()
    print("\n")
    r2 = Rhombus(40, 80)
    r2.printarea()
    r2.printperimeter()
    r2.get_sides()
    print("\n")
    t1 = Trapezoid(40, 80, 40, 20, 40)
    t1.printarea()
    t1.printperimeter()
    t1.get_sides()
    print("\n")

    rp1 = regPolygon(9, 30)
    rp1.printarea("Nonagon")
    rp1.printperimeter("nonagon")
    rp1.get_sides("nonagon")
    print("\n")
    s1 = Square()
    s1.diagonal()
    s1.printarea("Square")
    s1.printperimeter("square")
    print("\n")

    p1 = Pentagon()
    p1.no_diagonal()
    p1.printarea("Pentagon")
    p1.printperimeter("Pentagon")
    p1.get_sides("nonagon")
    print("\n")

    h1 = Pentagon()
    h1.no_diagonal()
    h1.printarea("Hexagon")
    h1.printperimeter("Hexagon")
    h1.get_sides("nonagon")
    print("\n")

    c1 = Circle(25)
    print("Printing area and circumference of Circle :")
    print(c1.area())
    print(c1.circumference())
    print("\n")

    e1 = Ellipse(25, 50)
    print("Printing area and circumference of ellipse :")

    print(e1.area())
    print(e1.circumference())
    print("\n")

    s = Sphere(5)
    print("Printing surface area of sphere:")
    print(s.surface_area())
