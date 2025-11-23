"""
Python OOP - Encapsulation

Demonstrates public, protected, and private attributes and methods.
"""


class BankAccount:
    """Bank account demonstrating encapsulation"""

    def __init__(self, owner, balance):
        self.owner = owner  # public
        self._balance = balance  # protected
        self.__password = "1234"  # private

    # Public method
    def deposit(self, amount):
        self._balance += amount

    # Protected method (convention)
    def _display_balance(self):
        return self._balance

    # Private method
    def __display_password(self):
        return self.__password


account = BankAccount("Alice", 1000)
account.deposit(500)
print("Balance:", account._display_balance())  # OK but by convention protected
# print(account.__display_password())           # ERROR: private
