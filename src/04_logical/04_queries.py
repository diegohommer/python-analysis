"""
A minimal demonstration of queries and search in Python.

Queries retrieve information from facts using comprehensions,
filtering, or generator expressions.
"""

# Knowledge base (facts)
parents = [
    ("alice", "bob"),
    ("bob", "carol"),
    ("carol", "david"),
]

if __name__ == "__main__":
    print("\n--- QUERIES DEMO ---\n")

    # List comprehension example
    children_of_alice = [c for p, c in parents if p == "alice"]
    print("Children of Alice:", children_of_alice)

    # Filter + lambda example
    def get_children(parent_name):
        return list(filter(lambda pair: pair[0] == parent_name, parents))

    print("Children of Bob:", [c for _, c in get_children("bob")])
