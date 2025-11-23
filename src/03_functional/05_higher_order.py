"""
Python Functional - Higher-Order Functions

Shows functions that accept other functions as arguments or return functions.
"""

# map - apply a function to all elements
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

# filter - select elements matching a condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# reduce - combine elements (from functools)
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)


# Function returning function
def make_multiplier(factor):
    return lambda x: x * factor


double = make_multiplier(2)
print("Double 5:", double(5))
