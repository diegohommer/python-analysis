"""
Python Functional - Lambda Functions

Demonstrates anonymous functions and basic usage.
"""

# Simple lambda
square = lambda x: x**2
print("Square of 5:", square(5))

# Lambda with multiple arguments
add = lambda a, b: a + b
print("Sum:", add(3, 4))

# Using lambda in sorting
names = ["Alice", "Bob", "Charlie"]
names.sort(key=lambda n: len(n))
print("Sorted by length:", names)
