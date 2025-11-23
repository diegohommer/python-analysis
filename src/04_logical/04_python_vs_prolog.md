# Python vs Prolog (Brief)

## Core Idea
Prolog is a pure logic language: programs define facts and rules, and the system solves queries through unification and backtracking. Python is multi-paradigm and does not have a native logic engine.

## Prolog
- Facts and rules are first-class language constructs.
- Execution model is inference: the system decides how to reach a solution.
- Example:

parent(alice, bob).
ancestor(X, Y) :- parent(X, Y).
?- ancestor(alice, bob).

## Python
- Must simulate logic manually (recursion, loops) or through libraries.
- Example pure Python approach: store facts in lists and infer via recursive functions.
- With libraries like kanren, Python can support:
  - logic variables
  - unification
  - relations
  - query evaluation

## Key Differences
- Prolog: declarative, inference drives execution.
- Python: imperative by default; logic must be implemented.
- Prolog searches automatically; Python must code search explicitly unless using a logic library.

## Conclusion
Both can solve logic problems, but Prolog is designed for logic from the ground up, while Python can emulate logic when needed.
