"""
Python OOP - Classes and Objects

This module demonstrates how to define classes and create objects.
"""


class Person:
    """Represents a person with a name and age."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        """Return a greeting string."""
        return f"Hello, my name is {self.name} and I'm {self.age} years old."


# Creating objects
alice = Person("Alice", 30)
bob = Person("Bob", 25)

print(alice.greet())
print(bob.greet())
