"""
Python Functional - Pattern Matching (Python 3.10+)

Demonstrates structural pattern matching using match/case.
"""


def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"Y={y} axis"
        case (x, 0):
            return f"X={x} axis"
        case (x, y):
            return f"Point at ({x}, {y})"
        case _:
            return "Unknown"


points = [(0, 0), (0, 5), (3, 0), (4, 7)]
for p in points:
    print(describe_point(p))
