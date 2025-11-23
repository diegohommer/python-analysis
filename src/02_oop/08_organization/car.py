"""
car.py

Defines the Car class.
"""


class Car:
    """Represents a car with a make and model."""

    def __init__(self, make, model):
        """
        Initialize a Car object.

        Args:
            make (str): The manufacturer of the car.
            model (str): The model name of the car.
        """
        self.make = make
        self.model = model

    def info(self):
        """
        Return a descriptive string for the car.

        Returns:
            str: Description of the car.
        """
        return f"Car: {self.make} {self.model}"
