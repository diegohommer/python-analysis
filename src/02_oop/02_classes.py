"""
Python OOP - Class, __init__ and __del__ demonstration

This module demonstrates how to define classes and create objects.
"""


class Person:
    """Represents a person with a name and age."""

    def __init__(self, name, age):
        """Constructor: called when a new object is created."""
        self.name = name
        self.age = age
        print(f"{self.name} has been created!")

    def greet(self):
        """Return a greeting string."""
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

    def __del__(self):
        """Destructor: called when the object is about to be destroyed."""
        print(f"{self.name} is being deleted.")


# Creating objects
alice = Person("Alice", 30)
bob = Person("Bob", 25)

print(alice.greet())
print(bob.greet())

# Deleting objects explicitly
del alice
del bob
