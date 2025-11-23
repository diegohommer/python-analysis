"""
Python OOP - Modules and Packages

Demonstrates how to organize code in modules and packages.
"""

# Imagine this file is inside package 'vehicles'


class Car:
    def drive(self):
        return "Driving a car"


class Bike:
    def ride(self):
        return "Riding a bike"


# You can import this module elsewhere:
# from vehicles.modules_packages import Car, Bike
car = Car()
bike = Bike()
print(car.drive())
print(bike.ride())
