"""
Python Essentials - Collections

This module covers the main Python collection types: list, tuple, dict, set.
It demonstrates creation, access, modification, and iteration over collections.
"""

# List - ordered, mutable
nums = [1, 2, 3, 4]
nums.append(5)
print("List:", nums)
print("First element:", nums[0])
print("Last element:", nums[-1])
print("Slicing [1:4]:", nums[1:4])

# Tuple - ordered, immutable
pt = (10, 20, 30)
print("\nTuple:", pt)
print("Access element:", pt[1])

# Dictionary - key-value pairs
person = {"name": "Alice", "age": 30, "city": "Paris"}
print("\nDictionary:", person)
print("Access value by key:", person["name"])
print("Get method:", person.get("email", "Not provided"))

# Set - unordered, unique elements
s = {1, 2, 3, 3, 2}
print("\nSet (duplicates removed):", s)
s.add(4)
print("Set after adding 4:", s)
s.remove(2)
print("Set after removing 2:", s)

# Iterating over collections
print("\nIterating over list:")
for n in nums:
    print(n, end=" ")

print("\nIterating over dict keys and values:")
for key, value in person.items():
    print(f"{key}: {value}")
