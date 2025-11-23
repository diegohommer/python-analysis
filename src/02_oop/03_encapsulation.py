"""
Python OOP - Encapsulation Demonstration
Public, protected, and private attributes and methods, with access examples.
"""


class BankAccount:
    """Bank account demonstrating encapsulation"""

    def __init__(self, owner, balance):
        self.owner = owner  # public
        self._balance = balance  # protected (by convention)
        self.__password = "1234"  # private (name mangling)

    # Public method
    def deposit(self, amount):
        self._balance += amount

    # Protected method (by convention)
    def _display_balance(self):
        return self._balance

    # Private method (name mangled)
    def __display_password(self):
        return self.__password


account = BankAccount("Alice", 1000)

# ------------------------------
# Public access
print("Public attribute 'owner':", account.owner)  # ✅ Works
account.deposit(500)  # ✅ Works
print("Balance via deposit:", account._balance)  # ⚠️ Direct access not recommended

# ------------------------------
# Protected access
print("Protected attribute '_balance':", account._balance)  # ⚠️ Works but discouraged
print(
    "Protected method '_display_balance':", account._display_balance()
)  # ⚠️ Works, but conventionally internal

# ------------------------------
# Private access (direct)
try:
    print(account.__password)  # ❌ AttributeError
except AttributeError as e:
    print("Direct private access failed:", e)

try:
    print(account.__display_password())  # ❌ AttributeError
except AttributeError as e:
    print("Direct private method access failed:", e)

# ------------------------------
# Private access via name mangling
print("Private attribute via name mangling:", account._BankAccount__password)  # ✅ Works
print("Private method via name mangling:", account._BankAccount__display_password())  # ✅ Works

# ------------------------------
# Summary
print("\nSummary:")
print("Public = fully accessible")
print("Protected = accessible but by convention should be internal")
print("Private = name mangled, harder to access, but still possible")
