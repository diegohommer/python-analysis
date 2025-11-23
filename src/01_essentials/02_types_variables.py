"""
Python Essentials - Variables and Types

This module introduces Python variables, dynamic typing, and common built-in types.
It demonstrates how to declare variables, check types, convert types, and use dynamic typing.
"""

# --- Basic Types ---
x = 10  # Integer
pi = 3.14159  # Float
name = "Alice"  # String
active = True  # Boolean

print("x:", x, "type:", type(x))
print("pi:", pi, "type:", type(pi))
print("name:", name, "type:", type(name))
print("active:", active, "type:", type(active))

# --- Type Conversion ---
print("\nType conversions:")
print("float(x):", float(x))
print("str(pi):", str(pi))
print("int(pi):", int(pi))

# --- Dynamic Typing ---
x = "Now I'm a string"
print("\nDynamic typing:")
print("x:", x, "type:", type(x))

# --- Complex Numbers ---
c = 3 + 4j
print("\nComplex number:", c, "type:", type(c))

# --- Everything is an Object ---
print("\nEverything in Python is an object:")

x = 42
print("Is x an object?", isinstance(x, object))

s = "hello"
print("Is s an object?", isinstance(s, object))


def greet():
    return "Hi"


print("Is greet an object?", isinstance(greet, object))


class Person:
    pass


print("Is Person an object?", isinstance(Person, object))

import math

print("Is math an object?", isinstance(math, object))

print("Is None an object?", isinstance(None, object))
