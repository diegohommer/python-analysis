"""
Python Functional - Immutability

Shows how to favor immutable data structures and avoid side-effects.
"""

# Tuple - immutable sequence
numbers = (1, 2, 3)
print("Original tuple:", numbers)

# Strings are immutable
text = "hello"
new_text = text.upper()
print("Original text:", text)
print("Uppercase:", new_text)


# Avoiding side-effects in functions
def add_to_list(lst, value):
    """Return a new list without modifying the original"""
    return lst + [value]


original = [1, 2, 3]
new_list = add_to_list(original, 4)
print("Original:", original)
print("New:", new_list)
