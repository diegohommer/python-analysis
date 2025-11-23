"""
Python Essentials - Strings

This module covers string creation, basic operations, formatting, 
and multiline strings. It also shows common string methods.
"""

# Basic string
s = "Hello, Python!"

print("Original:", s)
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Check if 'Python' is in s:", "Python" in s)
print("Check if 'Java' is in s:", "Java" in s)

# String formatting with f-strings
name = "Alice"
age = 30
greeting = f"My name is {name} and I am {age} years old."
print("\nFormatted string:", greeting)

# Multiline string
multiline = """This is line 1
This is line 2
This is line 3"""
print("\nMultiline string:\n", multiline)

# String methods
text = "  python is awesome  "
print("\nOriginal text:", repr(text))
print("Stripped text:", repr(text.strip()))
print("Capitalized:", text.capitalize())
print("Title:", text.title())
print("Replace:", text.replace("awesome", "great"))
print("Split:", text.split())
