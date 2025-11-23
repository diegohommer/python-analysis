"""
Python OOP - Inheritance, ABCs, super(), and Mixins

Shows single inheritance, multiple inheritance, and mixins.
"""

from abc import ABC, abstractmethod


# ----------------------
# Abstract Base Class
# ----------------------
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        """All animals must implement speak"""
        pass

    def info(self):
        return f"This is {self.name}"


# ----------------------
# Single Inheritance
# ----------------------
class Dog(Animal):
    def speak(self):
        return "Woof!"

    def info(self):
        # Call method from parent using super()
        return super().info() + " and it's a Dog"


dog = Dog("Rex")
print(dog.speak())  # Overridden method
print(dog.info())


# ----------------------
# Multiple Inheritance and Mixins
# ----------------------
class FlyMixin:
    def fly(self):
        return f"{self.name} is flying high!"


class SwimMixin:
    def swim(self):
        return f"{self.name} is swimming!"


class Bird(Animal, FlyMixin):
    def speak(self):
        return "Chirp!"


class Duck(Bird, SwimMixin):
    def speak(self):
        # Call Bird's speak with super()
        return super().speak() + " quack!"


bird = Bird("Tweety")
duck = Duck("Donald")

print(bird.speak())
print(bird.fly())

print(duck.speak())
print(duck.fly())
print(duck.swim())
