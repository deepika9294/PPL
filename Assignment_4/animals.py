from abc import ABC, abstractmethod


class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def type(self):
        pass

    def is_endangered(self):
        pass

    def food(self):
        pass


class Cat(animal):
    legs = 4

    def info(self):
        print(
            f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

    def type(self):
        print("Terrestrial")

    def is_endangered(self):
        return False

    def food(self):
        print("Rat, milk")


class Dog(animal):
    legs = 4

    def info(self):
        print(
            f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

    def type(self):
        print("Terrestrial")

    def is_endangered(self):
        return False

    def food(self):
        print('Bone Broth, Raw Goat Milk')


class Wild(animal):
    legs = 4

    def food(self):
        print("Most of them eat other animals living in the jungle")

    def type(self):
        print('Mammal')

    def is_endangered(self):
        pass


class Lion(Wild):
    def is_endangered(self):
        return True

    def sound(self):
        print("Roar")

    def famous(self):
        print("famous as king of jungle")


class Reptile(animal):
    def type(self):
        print("Vertebrates")

    def scales(self):
        print("all reptiles have scales")


class Snake(Reptile):
    def famous(self):
        print("Venomous snakes are used for making vaccines")


class Elephant(Wild):
    def famous(self):
        print("World's  largest land animal")

    def food(self):
        print("Plants, Grass")

    def other_qualities(self):
        print("Their tusks never stop growing")

    def is_endangered(self):
        return False


class Bird(ABC):
    @abstractmethod
    def can_fly(self):
        pass

    def type(self):
        print("Aves")

    def wings(self):
        print("All birds have wings, although not all birds fly. ")

    @abstractmethod
    def beak_type(self):
        pass

    @abstractmethod
    def bird_property(self):
        pass


class Ostrich(Bird):
    def can_fly(self):
        return False

    def beak_type(self):
        print("Broad beak with rounded tip")

    def bird_property(self):
        print("Tallest bird")


if __name__ == "__main__":
    c = Cat("catty", 5)
    c.make_sound()
    c.type()
    c.is_endangered()
    c.food()
    print("\n")

    d = Dog("Tom", 5)
    d.make_sound()
    d.type()
    d.is_endangered()
    d.food()
    print("\n")

    w = Wild("something", 15)
    w.food()
    w.type()
    print("\n")

    l = Lion("king", 20)
    l.is_endangered()
    l.sound()
    l.famous()
    print("\n")

    o = Ostrich()
    o.beak_type()
    o.bird_property()
    print("\n")

    el = Elephant("Ella", 17)
    el.famous()
    el.food()
    el.other_qualities()
    el.is_endangered()
    print("\n")

    rep = Reptile("repu", 3)
    rep.type()
    rep.scales()
    snake1 = Snake("saa", 7)
    snake1.famous()
