"""
Python OOP - Universal Polymorphism

Demonstrates duck typing: any object implementing the expected methods can be used.
"""


class Bird:
    def fly(self):
        return "Flap flap"

    def __str__(self):
        return "Bird"


class Airplane:
    def fly(self):
        return "Jet engine!"

    def __str__(self):
        return "Airplane"


class SuperHero:
    def fly(self):
        return "Superhero soaring!"

    def __str__(self):
        return "SuperHero"


# ----------------------
# Polymorphic function: works with any object that has a fly() method
# ----------------------
def lets_fly(entity):
    # Universal polymorphism (duck typing): entity.fly() works for any compatible object
    print(f"{entity}: {entity.fly()}")


# ----------------------
# Test: polymorphism in action
# ----------------------
if __name__ == "__main__":
    entities = [Bird(), Airplane(), SuperHero()]
    for e in entities:
        # Each call lets_fly(e) behaves differently depending on the actual object type
        lets_fly(e)
