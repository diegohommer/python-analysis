"""
A minimal demonstration of logic programming concepts in pure Python.

This simulates a tiny Prolog-like environment using:
- Facts
- Rules
- Queries
- Recursive inference

This is *not* a full logic language, but it demonstrates how
Python can emulate logical reasoning.
"""

# Knowledge base (facts)
parents = [
    ("alice", "bob"),
    ("bob", "carol"),
    ("carol", "david"),
]


def is_parent(parent, child):
    """Direct parent relationship (simple fact lookup)."""
    return (parent, child) in parents


def is_ancestor(ancestor, person):
    """
    Logical rule:
    A is ancestor of B if:
        - A is direct parent of B
        - OR A is ancestor of the parent of B
    """
    # Base case
    if is_parent(ancestor, person):
        return True

    # Recursive inference rule
    for p, c in parents:
        if c == person and is_ancestor(ancestor, p):
            return True

    return False


if __name__ == "__main__":
    print("\n--- PURE PYTHON LOGIC DEMO ---\n")

    print("Is alice parent of bob?", is_parent("alice", "bob"))
    print("Is alice ancestor of david?", is_ancestor("alice", "david"))
    print("Is bob ancestor of david?", is_ancestor("bob", "david"))
    print("Is carol ancestor of alice?", is_ancestor("carol", "alice"))  # False

    print("\nExplanation:")
    print(" - Facts define direct parent relationships.")
    print(" - is_ancestor() uses a rule similar to Prolog.")
    print(" - The query returns where the rule evaluates as True.")
