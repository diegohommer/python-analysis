"""
A minimal demonstration of rules in pure Python.

Rules are functions that define derived relationships
based on existing facts, optionally using recursion.
"""

# Knowledge base (facts)
parents = [
    ("alice", "bob"),
    ("bob", "carol"),
    ("carol", "david"),
]


def is_grandparent(grandparent, grandchild):
    """Return True if grandparent is a parent of a parent of grandchild."""
    for p, c in parents:
        if p == grandparent:
            for p2, c2 in parents:
                if p2 == c and c2 == grandchild:
                    return True
    return False


if __name__ == "__main__":
    print("\n--- RULES DEMO ---\n")
    print("Is Alice grandparent of Carol?", is_grandparent("alice", "carol"))
    print("Is Bob grandparent of David?", is_grandparent("bob", "david"))
