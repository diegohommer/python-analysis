"""
A minimal demonstration of pattern matching for logic-like queries.

Python 3.10's match statement allows inspecting and destructuring
data structures in a declarative style.
"""

# Knowledge base (facts)
parents = [
    ("alice", "bob"),
    ("bob", "carol"),
    ("carol", "david"),
]


def find_parent_of(person):
    """Return the parent of a given person using pattern matching."""
    for pair in parents:
        match pair:
            case (p, c) if c == person:
                return p
    return None


if __name__ == "__main__":
    print("\n--- PATTERN MATCHING DEMO ---\n")
    print("Parent of Carol:", find_parent_of("carol"))
    print("Parent of Bob:", find_parent_of("bob"))
