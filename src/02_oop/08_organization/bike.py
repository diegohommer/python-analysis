"""
bike.py

Defines the Bike class.
"""


class Bike:
    """Represents a bike with brand and type."""

    def __init__(self, brand, type_):
        """
        Initialize a Bike object.

        Args:
            brand (str): The manufacturer/brand of the bike.
            type_ (str): Type of the bike (e.g., Mountain, Road).
        """
        self.brand = brand
        self.type_ = type_

    def info(self):
        """
        Return a descriptive string for the bike.

        Returns:
            str: Description of the bike.
        """
        return f"Bike: {self.brand} ({self.type_})"
