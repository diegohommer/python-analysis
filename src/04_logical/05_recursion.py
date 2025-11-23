"""
A minimal demonstration of recursion for logical inference in Python.

Recursion allows defining transitive relationships,
such as ancestors or hierarchical paths.
"""

# Knowledge base (facts)
parents = [
    ("alice", "bob"),
    ("bob", "carol"),
    ("carol", "david"),
]


def ancestors(person):
    """Return a list of all ancestors of a given person."""
    result = []
    for p, c in parents:
        if c == person:
            result.append(p)
            result.extend(ancestors(p))
    return result


if __name__ == "__main__":
    print("\n--- RECURSION DEMO ---\n")
    print("Ancestors of David:", ancestors("david"))
    print("Ancestors of Carol:", ancestors("carol"))
