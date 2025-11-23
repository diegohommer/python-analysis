"""
Python Essentials - Functions

This module explains how to define functions, use default and keyword arguments,
return values, and demonstrates first-class functions.
"""


# Simple function
def greet(name="world"):
    """Return a greeting string."""
    return f"Hello {name}"


print(greet())
print(greet("Alice"))


# Function with keyword argument
def power(base, exp=2):
    """Return base raised to the exponent exp."""
    return base**exp


print("3^3 =", power(3, 3))
print("4^2 =", power(4))  # default exponent

# Functions as first-class objects
f = greet
print(f("Bob"))


# Function returning multiple values
def min_max(numbers):
    """Return both the minimum and maximum of a list."""
    return min(numbers), max(numbers)


numbers = [3, 5, 1, 9]
minimum, maximum = min_max(numbers)
print("Min:", minimum, "Max:", maximum)
