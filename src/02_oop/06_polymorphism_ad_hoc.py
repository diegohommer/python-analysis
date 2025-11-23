"""
Python OOP - Ad-hoc Polymorphism

Demonstrates method overriding in subclasses (ad-hoc polymorphism).
"""


class Shape:
    """Base class for geometric shapes"""

    def area(self):
        return 0  # Default implementation (polymorphic method)

    def __str__(self):
        return "Base Shape"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # ----------------------
    # Ad-hoc polymorphism: overriding the base class method
    # ----------------------
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # ----------------------
    # Ad-hoc polymorphism: overriding the base class method
    # ----------------------
    def area(self):
        return 3.14159 * self.radius**2

    def __str__(self):
        return f"Circle({self.radius})"


# ----------------------
# Test: polymorphic behavior via method calls
# ----------------------
if __name__ == "__main__":
    shapes = [Rectangle(3, 4), Circle(5), Shape()]
    for shape in shapes:
        # Polymorphism happens here: same call shape.area() behaves differently depending on the actual object type
        print(f"{shape}: area = {shape.area()}")
