"""
Python OOP - Properties and Decorators

Demonstrates @property, @staticmethod, and @classmethod.
"""


# ----------------------
# Class with property
# ----------------------
class Person:
    """Represents a person with a name and age."""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # ----------------------
    # Getter
    # ----------------------
    @property
    def age(self):
        return self._age

    # ----------------------
    # Setter
    # ----------------------
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    # ----------------------
    # Class method
    # ----------------------
    @classmethod
    def create_baby(cls, name):
        """Factory method to create a baby with age 0"""
        return cls(name, 0)

    # ----------------------
    # Static method
    # ----------------------
    @staticmethod
    def is_adult(age):
        """Check if given age qualifies as adult"""
        return age >= 18


# ----------------------
# Test / Demonstration
# ----------------------
if __name__ == "__main__":
    p = Person("Alice", 30)
    print(f"{p._name} is {p.age} years old")  # Using getter

    p.age = 31  # Using setter
    print(f"Next year: {p.age}")

    # Class method
    baby = Person.create_baby("Bob")
    print(f"{baby._name} is {baby.age} years old")

    # Static method
    print(Person.is_adult(20))  # True
    print(Person.is_adult(10))  # False
