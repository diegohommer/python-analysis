"""
Python Functional - Recursion

Demonstrates using recursion to solve problems.
"""


# Factorial using recursion
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))


# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci(7):", fibonacci(7))
