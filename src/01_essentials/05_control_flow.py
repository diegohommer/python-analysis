"""
Python Essentials - Control Flow

This module demonstrates Python's control flow structures: if/else, for loops,
while loops, and usage of break and continue.
"""

x = 7

# If / Else
if x > 10:
    print("x is big")
elif x > 5:
    print("x is medium")
else:
    print("x is small")

# For loop
print("\nFor loop:")
for i in range(5):
    print(i, end=" ")

# While loop
print("\n\nWhile loop:")
counter = 5
while counter > 0:
    print(counter, end=" ")
    counter -= 1

# break and continue
print("\n\nBreak and continue:")
for i in range(5):
    if i == 2:
        continue  # Skip 2
    if i == 4:
        break  # Stop loop
    print(i, end=" ")
