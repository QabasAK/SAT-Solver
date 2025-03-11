# SAT-Solver

A Boolean SAT solver that determines the satisfiability of propositional logic formulas in CNF (Conjuctive Normal Form) using both the **DPLL (Davis-Putnam-Logemann-Loveland)** algorithm and the **CDCL (Conflict-Driven Clause Learning)** algorithm.

### DPLL Algorithm 
Implements pure **literal elimination** and **unit propagation**. Uses a vector of clauses to store the CNF formula.

### CDCL Algorithm 
Implements **conflict analysis**, **clause learning** and **non-chronological backtracking**. Uses a structured approach to track assignments, including *value*, *reason* and *level*. It performs **1-UIP (Unique Implication Point)** learning for effective clause learning. 

### Benchmarking & Visualization 
The solvers were evaluated against **SATLIB test cases** with **chrono-based runtime measurements** and built using Manim to animate SAT solver steps (rendered with LaTeX-based representation).

### Future Work 
+ Implementing watched literals to improve unit propagation efficiency.
+ Add a learned clause database with deletion heuristics (LBD).
+ Introducing restart strategies for better solver performance.

