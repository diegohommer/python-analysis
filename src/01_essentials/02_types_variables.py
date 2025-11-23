"""
Python Essentials - Variables and Types

This module introduces Python variables, dynamic typing, and common built-in types.
It demonstrates how to declare variables, check types, convert types, and use dynamic typing.
"""

# Integer
x = 10
# Float
pi = 3.14159
# String
name = "Alice"
# Boolean
active = True

print("x:", x, "type:", type(x))
print("pi:", pi, "type:", type(pi))
print("name:", name, "type:", type(name))
print("active:", active, "type:", type(active))

# Type conversion
print("\nType conversions:")
print("float(x):", float(x))
print("str(pi):", str(pi))
print("int(pi):", int(pi))

# Dynamic typing
x = "Now I'm a string"
print("\nDynamic typing:")
print("x:", x, "type:", type(x))

# Python also supports complex numbers
c = 3 + 4j
print("\nComplex number:", c, "type:", type(c))
