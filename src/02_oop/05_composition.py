"""
Python OOP - Composition

Shows how classes can contain other objects.
"""


class Engine:
    def start(self):
        return "Engine started"


class Car:
    def __init__(self, make, engine):
        self.make = make
        self.engine = engine  # Composition: Car has an Engine

    def start(self):
        return f"{self.make}: {self.engine.start()}"


engine = Engine()
car = Car("Toyota", engine)
print(car.start())
