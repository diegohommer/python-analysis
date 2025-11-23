"""
Python OOP - Polymorphism

Demonstrates ad-hoc and universal polymorphism.
"""


# Ad-hoc polymorphism (method overriding)
class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r**2


shapes = [Rectangle(3, 4), Circle(5)]
for shape in shapes:
    print("Area:", shape.area())


# Universal polymorphism (duck typing)
class Bird:
    def fly(self):
        return "Flap flap"


class Airplane:
    def fly(self):
        return "Jet engine!"


def lets_fly(entity):
    print(entity.fly())


lets_fly(Bird())
lets_fly(Airplane())
