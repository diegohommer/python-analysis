"""
Python OOP - Delegation and Callbacks

Demonstrates passing functions, methods, and callable objects as arguments
to delegate behavior or handle events.
"""


# ----------------------
# Simple function callback
# ----------------------
def greet(name):
    return f"Hello, {name}!"


def run_callback(callback, *args, **kwargs):
    """
    Executes the given callback with provided arguments.

    Args:
        callback (callable): Function, method, or object with __call__.
        *args, **kwargs: Arguments to pass to the callback.

    Returns:
        The result of callback(*args, **kwargs)
    """
    return callback(*args, **kwargs)


# ----------------------
# Callable object
# ----------------------
class Multiplier:
    """Callable object that multiplies a number by a given factor."""

    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor


# ----------------------
# Test / Demonstration
# ----------------------
if __name__ == "__main__":
    # Passing a simple function
    print(run_callback(greet, "Alice"))  # Hello, Alice!

    # Passing a lambda
    print(run_callback(lambda x, y: x + y, 5, 7))  # 12

    # Passing a callable object
    doubler = Multiplier(2)
    print(run_callback(doubler, 10))  # 20
