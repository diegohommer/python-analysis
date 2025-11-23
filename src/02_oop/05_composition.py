"""
Python OOP - Composition

Demonstrates how classes can contain and use other objects to build complex behavior.
"""


# ----------------------
# Component Classes
# ----------------------
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} HP started"

    def stop(self):
        return "Engine stopped"


class GPS:
    def __init__(self, model):
        self.model = model

    def locate(self, destination):
        return f"Routing to {destination} using {self.model} GPS"


class Radio:
    def play_music(self, song):
        return f"Playing '{song}' on radio"


# ----------------------
# Composed Class
# ----------------------
class Car:
    def __init__(self, make, engine, gps=None, radio=None):
        self.make = make
        self.engine = engine  # Composition: Car has an Engine
        self.gps = gps  # Optional composition
        self.radio = radio  # Optional composition

    def start(self):
        return f"{self.make}: {self.engine.start()}"

    def stop(self):
        return f"{self.make}: {self.engine.stop()}"

    def navigate(self, destination):
        if self.gps:
            return self.gps.locate(destination)
        return f"{self.make} has no GPS installed"

    def play_music(self, song):
        if self.radio:
            return self.radio.play_music(song)
        return f"{self.make} has no radio installed"


# ----------------------
# Using the Classes
# ----------------------
# Create components
engine_v6 = Engine(300)
gps_nav = GPS("Garmin")
radio_pioneer = Radio()

# Compose car objects
car1 = Car("Toyota", engine_v6, gps_nav, radio_pioneer)
car2 = Car("Honda", Engine(200))  # Only engine

# Interactions
print(car1.start())
print(car1.navigate("Paris"))
print(car1.play_music("Bohemian Rhapsody"))
print(car1.stop())

print("---")

print(car2.start())
print(car2.navigate("London"))
print(car2.play_music("Imagine"))
print(car2.stop())
