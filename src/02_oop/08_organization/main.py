"""
main.py

Demonstrates code organization using separate modules.
Imports Car and Bike classes from their modules and uses them.
"""

# Import classes from modules
from car import Car
from bike import Bike

# ----------------------
# Create objects
# ----------------------
car = Car("Toyota", "Corolla")
bike = Bike("Trek", "Mountain")

# ----------------------
# Use the objects
# ----------------------
print(car.info())  # Output: Car: Toyota Corolla
print(bike.info())  # Output: Bike: Trek (Mountain)
