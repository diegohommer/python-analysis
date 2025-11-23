from kanren import Relation, facts, run, var, lall

# --- Define the relation ---
# We create a logical relation "parent" (parent-child)
parent = Relation()

# --- Insert facts into the knowledge base ---
# Each tuple represents (parent, child)
facts(
    parent,
    ("alice", "bob"),
    ("bob", "carol"),
    ("carol", "david"),
)


# --- Define rules ---
# Example: "grandparent" is someone who is a parent of a parent
def grandparent(gp, gc):
    x = var()
    # gp is grandparent of gc if there exists x such that
    # gp is parent of x and x is parent of gc
    return lall(parent(gp, x), parent(x, gc))


if __name__ == "__main__":
    print("\n--- KANREN LOGIC PROGRAMMING DEMO ---\n")

    # --- Simple query ---
    x = var()
    print("Who are the children of Alice?")
    result = run(0, x, parent("alice", x))
    print("Result:", result)

    # --- Multi-variable query ---
    parent_var = var()
    child_var = var()
    print("\nAll parent-child pairs:")
    result_all = run(0, (parent_var, child_var), parent(parent_var, child_var))
    print(result_all)

    # --- Query using a rule ---
    gp = var()
    gc = var()
    print("\nWho are the grandchildren of Alice?")
    result_grandchildren = run(0, gc, grandparent("alice", gc))
    print("Result:", result_grandchildren)

    print("\nKanren automatically performs unification and search.")
