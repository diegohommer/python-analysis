from kanren import Relation, facts, run, var

# Define relation
parent = Relation()

# Insert facts into the knowledge base
facts(
    parent,
    ("alice", "bob"),
    ("bob", "carol"),
    ("carol", "david"),
)


if __name__ == "__main__":
    print("\n--- KANREN LOGIC PROGRAMMING DEMO ---\n")

    # Single variable query
    x = var()
    print("Who are the children of alice?")
    result = run(0, x, parent("alice", x))
    print("Result:", result)

    print("\nAll parent-child pairs:")

    # Multi-variable query
    parent_var = var()
    child_var = var()

    result_all = run(0, (parent_var, child_var), parent(parent_var, child_var))
    print(result_all)

    print("\nKanren automatically performs unification and search.")
