import turtle
# Classes Based on Animals


class Animal:
    def __init__(self):
        # Private
        self.__kingdom = ""
        # Protected
        self._lifespan = ""
        # Public
        # name means which animal it is
        self.name = ""

    # setters
    def set_kingdom(self, kingdom):
        self.__kingdom = kingdom

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan

    # getters

    def get_kingdom(self):
        print("Animal Kingdom is " + self.__kingdom)

    def get_name(self):
        print("Animal name is " + self.name)

    def get_lifespan(self):
        print("Lifespan is " + self._lifespan)


# Derived classes
class Dog(Animal):

    def set_name(self):
        self.name = "Dog"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan

    # Accessing protecting member
    def get_name(self):
        print("Animal is: " + self.name)

    def animalProperty(self):
        print("Dog Barks")


class Lizard(Animal):
    def set_name(self):
        self.name = "Lizard"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan

   # Accessing protecting member

    def get_name(self):
        print("Animal is: " + self.name)

    def animalProperty(self):
        print("Lizard crawls")


class Butterfly(Animal):
    def set_name(self):
        self.name = "Butterfly"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan
   # Accessing protecting member

    def get_name(self):
        print("Animal is: " + self.name)

    def animalProperty(self):
        print("Butterflies are beautiful")


class Monkey(Animal):
    def set_name(self):
        self.name = "Monkey"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan
   # Accessing protecting member

    def get_name(self):
        print("Animal is: " + self.name)

    def animalProperty(self):
        print("Monkeys Jumps a alot")


class Cat(Animal):
    def set_name(self):
        self.name = "Cat"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan

   # Accessing protecting member
    def get_name(self):
        print("Animal is: " + self.name)

    def animalProperty(self):
        print("Cat drinks Milk")


class Camel(Animal):
    def set_name(self):
        self.name = "Camel"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan

   # Accessing protecting member

    def get_name(self):
        print("Animal is: " + self.name)

    def animalProperty(self):
        print("Camels usually found in desert")


class Peacock(Animal):
    def set_name(self):
        self.name = "Peacock"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan

   # Accessing protecting member

    def get_name(self):
        print("Animal is: " + self.name)

    def animalProperty(self):
        print("Peacock is a bird")


class Crow(Animal):
    def set_name(self):
        self.name = "Crow"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan

   # Accessing protecting member

    def get_name(self):
        print("Animal is: " + self.name)

    def animalProperty(self):
        print("Crows are black")


class Vulture(Animal):
    def set_name(self):
        self.name = "Vulture"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan

   # Accessing protecting member
    def get_name(self):
        print("Animal is: " + self.name)

    def animalProperty(self):
        print("Vulture eats carrion")


class Lion(Animal):
    def set_name(self):
        self.name = "Lion"

    def set_lifespan(self, lifespan):
        self._lifespan = lifespan

   # Accessing protecting member
    def get_name(self):
        print("Animal is: " + self.name)

    def animalProperty(self):
        print("Lion is king")

# ---------------------------------------------------------------------------------------------------------------------------------

# classes for shapes


class Shapes:
    def __init__(self):
        self._name = ''  # Protected member

    def get_name(self):
        print(self._name)


# Triangle
class Triangle(Shapes):
    def __init__(self):
        self._side = 3
        self._sideLength = 10
    # We can access protected members

    def set_name(self):
        self._name = 'Triangle'

    def get_side(self):
        print(self._side)

    def draw(self):
        t = turtle
        for _ in range(3):
            t.forward(self._sideLength)
            t.left(120)
        t.done()
        try:
            t.exitonclick()
        except:
            pass


class Pentagon(Shapes):
    def __init__(self):
        self._side = 5
        self._sideLength = 30
    # We can access protected members

    def set_name(self):
        self._name = 'Pentagon'

    def get_side(self):
        print(self._side)

    def draw(self):
        t = turtle
        for _ in range(5):
            t.forward(self._sideLength)
            t.left(72)
        t.done()
        try:
            t.exitonclick()
        except:
            pass


class Hexagon(Shapes):
    def __init__(self):
        self._side = 6
        self._sideLength = 30
    # We can access protected members

    def set_name(self):
        self._name = 'Hexagon'

    def get_side(self):
        print(self._side)

    def draw(self):
        t = turtle
        for _ in range(6):
            t.forward(self._sideLength)
            t.left(60)
        t.done()
        try:
            t.exitonclick()
        except:
            pass


class Heptagon(Shapes):
    def __init__(self):
        self._side = 7
        self._sideLength = 30
    # We can access protected members

    def set_name(self):
        self._name = 'Heptagon'

    def get_side(self):
        print(self._side)

    def draw(self):
        t = turtle
        for _ in range(7):
            t.forward(self._sideLength)
            t.left(51.42)
        t.done()
        try:
            t.exitonclick()
        except:
            pass


class Octagon(Shapes):
    def __init__(self):
        self._side = 5
        self._sideLength = 30
    # We can access protected members

    def set_name(self):
        self._name = 'Octagon'

    def get_side(self):
        print(self._side)

    def draw(self):
        t = turtle
        for _ in range(8):
            t.forward(self._sideLength)
            t.left(45)
        t.done()
        try:
            t.exitonclick()
        except:
            pass


class Equilateral(Triangle):
    # We have access to protected members
    def set_name(self):
        self._name = 'Equilateral Triangle'

    def get_side(self):
        print(self._side)

    def draw(self):
        t = turtle
        for _ in range(3):
            t.forward(self._sideLength)
            t.left(120)
        t.done()
        try:
            t.exitonclick()
        except:
            pass

# Circle


class Circle(Shapes):
    def __init__(self):
        self.__r = 0

    def set_name(self):
        self._name = 'Circle'

    def set_radius(self, r):
        self.__r = r

    def get_area(self):
        print(3.14 * (self.__r)**2)

    def draw(self):
        t = turtle
        t.circle(self.__r)
        t.done()
        try:
            t.exitonclick()
        except:
            pass

# Ellipse


class Ellipse(Shapes):
    def __init__(self):
        self.__a = 0
        self.__b = 0

    def set_name(self):
        self._name = 'Ellipse'

    def set_params(self, a, b):
        self.__a = a
        self.__b = b

    def get_area(self):
        print(3.14 * self.__a * self.__b)

    def get_name(self):
        print(self._name)

    def draw(self):
        t = turtle
        t.right(45)
        for _ in range(2):
            t.circle(self.__a, 90)
            t.circle(self.__b, 90)
        t.done()
        try:
            t.exitonclick()
        except:
            pass

# Rectangle


class Rectangle(Shapes):
    def __init__(self):
        self.__side = 4
        self.__a = 10
        self.__b = 20
    # We have access to protected members

    def set_name(self):
        self._name = 'Rectangle'

    def get_side(self):
        print(self.__side)

    def draw(self):
        t = turtle
        t.forward(self.__a)
        t.left(90)
        t.forward(self.__b)
        t.left(90)
        t.forward(self.__a)
        t.left(90)
        t.forward(self.__b)
        t.left(90)
        t.done()
        try:
            t.exitonclick()
        except:
            pass


class Square(Rectangle):
    def __init__(self):
        self.sides = 4
        self.a = 10
    # We have access to protected members

    def set_name(self):
        self._name = 'Square'

    def get_side(self):
        print(self.sides)

    def draw(self):
        t = turtle
        for _ in range(4):
            t.forward(self.a)
            t.left(90)
        t.done()
        try:
            t.exitonclick()
        except:
            pass


if __name__ == "__main__":
    a1 = Animal()
    a1.set_kingdom("Mammal")
    a1.set_lifespan("20")
    # accesing private and public members with setters and getter, as they are not accessible outside the class
    a1.get_kingdom()
    a1.get_lifespan()
    print("\n")

    d1 = Dog()
    d1.set_name()
    d1.get_name()
    d1.set_lifespan("20")
    d1.get_lifespan()
    d1.animalProperty()
    print("\n")

    liz1 = Lizard()
    liz1.set_name()
    liz1.get_name()
    liz1.set_lifespan("10")
    liz1.get_lifespan()
    liz1.animalProperty()
    print("\n")

    b1 = Butterfly()
    b1.set_name()
    b1.get_name()
    b1.set_lifespan("2")
    b1.get_lifespan()
    b1.animalProperty()
    print("\n")

    monkey1 = Monkey()
    monkey1.set_name()
    monkey1.get_name()
    monkey1.set_lifespan("20")
    monkey1.get_lifespan()
    monkey1.animalProperty()
    print("\n")

    cat1 = Cat()
    cat1.set_name()
    cat1.get_name()
    cat1.set_lifespan("10")
    cat1.get_lifespan()
    cat1.animalProperty()
    print("\n")

    camel1 = Camel()
    camel1.set_name()
    camel1.get_name()
    camel1.set_lifespan("17")
    camel1.get_lifespan()
    camel1.animalProperty()
    print("\n")

    peacock1 = Peacock()
    peacock1.set_name()
    peacock1.get_name()
    peacock1.set_lifespan("10")
    peacock1.get_lifespan()
    peacock1.animalProperty()
    print("\n")

    crow1 = Crow()
    crow1.set_name()
    crow1.get_name()
    crow1.set_lifespan("10")
    crow1.get_lifespan()
    crow1.animalProperty()
    print("\n")

    v1 = Vulture()
    v1.set_name()
    v1.get_name()
    v1.set_lifespan("10")
    v1.get_lifespan()
    v1.animalProperty()
    print("\n")

    l1 = Lion()
    l1.set_name()
    l1.get_name()
    l1.set_lifespan("25")
    l1.get_lifespan()
    l1.animalProperty()
    print("\n")

# ------------------------------------------------------------------------------------------------------------

print("Printing shapes classes details")

e1 = Equilateral()
e1.set_name()
e1.get_name()
print("side is", end="")
e1.get_side()
e1.draw()
print("\n")


t1 = Triangle()
t1.set_name()
t1.get_name()
print("side is", end="")
t1.get_side()
t1.draw()
print("\n")

p1 = Pentagon()
p1.set_name()
p1.get_name()
print("side is", end="")
p1.get_side()
p1.draw()
print("\n")


h1 = Hexagon()
h1.set_name()
h1.get_name()
print("side is", end="")
h1.get_side()
h1.draw()
print("\n")


h = Heptagon()
h.set_name()
h.get_name()
print("side is", end="")
h.get_side()
h.draw()
print("\n")


o1 = Octagon()
o1.set_name()
o1.get_name()
print("side is", end="")
o1.get_side()
o1.draw()
print("\n")


r1 = Rectangle()
r1.set_name()
r1.get_name()
print("side is", end="")
r1.get_side()
r1.draw()
print("\n")


s1 = Square()
s1.set_name()
s1.get_name()
print("side is", end="")
s1.get_side()
s1.draw()
print("\n")


ell1 = Ellipse()
ell1.set_name()
ell1.get_name()
ell1.set_params(40, 80)
print("Area is", end="")
ell1.get_area()
ell1.draw()
print("\n")


c1 = Circle()
c1.set_name()
c1.get_name()
c1.set_radius(20)
print("Area is", end="")
c1.get_area()
c1.draw()
print("\n")
