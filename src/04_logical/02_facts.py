"""
A minimal demonstration of representing facts in pure Python.

Facts are basic relationships stored as tuples, lists, or dictionaries.
Queries and inference can be built on top of these structures.
"""

# Knowledge base (facts)
parents = [
    ("alice", "bob"),
    ("bob", "carol"),
    ("carol", "david"),
]

if __name__ == "__main__":
    print("\n--- FACTS DEMO ---\n")
    print("All parent-child pairs:")
    for p, c in parents:
        print(f"{p} is parent of {c}")
