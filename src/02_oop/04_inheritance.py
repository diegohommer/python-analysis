"""
Python OOP - Inheritance and Mixins

Shows single inheritance, multiple inheritance, and mixins.
"""


# Single inheritance
class Animal:
    def speak(self):
        return "Some generic sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


dog = Dog()
print(dog.speak())  # Overridden method


# Multiple inheritance and mixin
class FlyMixin:
    def fly(self):
        return "Flying high!"


class Bird(Animal, FlyMixin):
    def speak(self):
        return "Chirp!"


bird = Bird()
print(bird.speak())
print(bird.fly())
