# Logical Programming Overview

Logical programming is a programming paradigm based on:

- **Facts**
- **Rules**
- **Queries**
- **Inference**

Instead of telling the computer *how* to solve a problem (as in imperative programming), the programmer declares *what is true* and the runtime system determines the solution.

The most famous logic programming language is **Prolog**, where execution is based on:

- Horn clauses
- Unification
- Backtracking search

## Comparison with Python

Python is not a logic programming language, but it *can emulate* many of the same concepts through:

- Recursion
- Search mechanisms
- Pattern matching (`match` statements)
- Libraries such as `kanren` or `pyDatalog`
- Rule engines implemented in Python

This folder contains:

1. A pure-Python logic simulation (files 02 to 06)
2. A demo using the `kanren` logic library (file 07)
