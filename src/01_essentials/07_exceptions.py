"""
Python Essentials - Exceptions

This module introduces exception handling using try/except/finally and raising custom errors.
"""

# Handling exceptions
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Caught exception:", e)
finally:
    print("This always executes")


# Raising a custom exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age is {age}")


check_age(25)
# check_age(-5)  # Uncomment to test ValueError
