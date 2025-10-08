# Solving 3-SAT with Stochastic Hill Climbing: A Summary

This document outlines the theoretical and algorithmic foundations for solving the 3-Satisfiability (3-SAT) problem using the Stochastic Hill Climbing local search algorithm.

---

## 1. The 3-SAT Problem 🧩

**3-SAT** is a classic NP-Complete problem. The goal is to find a satisfying truth assignment for a given Boolean formula.

* **Formal Definition:**
    * We have a set of **Boolean variables** $V = \{x_1, x_2, \dots, x_n\}$.
    * A **literal** is a variable ($x_i$) or its negation ($\neg x_i$).
    * A **clause**, $C_j$, is a disjunction (OR) of exactly three literals: $C_j = (l_1 \lor l_2 \lor l_3)$.
    * The final **formula**, $\Phi$, is a conjunction (AND) of $m$ clauses in Conjunctive Normal Form (CNF):
        $$ \Phi = C_1 \land C_2 \land \dots \land C_m $$

* **Objective:** Find a truth assignment (e.g., $x_1=\text{True}, x_2=\text{False}, \dots$) that makes the entire formula $\Phi$ evaluate to `True`. This requires **every single clause** to be satisfied.

---

## 2. The Stochastic Hill Climbing Algorithm ⛰️

This is a local search heuristic perfect for problems where we can define a "state" and a "score."

* **Core Concepts Mapped to 3-SAT:**
    * **State:** A complete truth assignment for all $n$ variables (e.g., an array `[True, False, ..., True]`).
    * **Objective Function (Score):** The number of clauses satisfied by a given assignment. The goal is to maximize this score to $m$.
    * **Neighbor:** A state that can be reached by flipping the value of a single variable in the current state. Each state has $n$ neighbors.

* **Key Differentiator:**
    * **Greedy Hill Climbing:** Always chooses the *single best* neighboring state (the one with the highest score).
    * **Stochastic Hill Climbing:** Identifies *all* neighboring states that are better than the current one and then **randomly picks one** from that list. This randomness is its key feature.

---

## 3. The Core Logic: How It Works

Here is the step-by-step logic that we clarified.

1.  **Initialization:** Start with a randomly generated truth assignment (`current_state`).

2.  **Evaluation:** Calculate its score, `current_score`, which is the number of satisfied clauses.

3.  **Neighbor Selection (The Crucial Part):**
    * **a) Deterministic Filtering:** Create a candidate list, `uphill_moves`, containing every neighbor whose score is **strictly greater than** `current_score`.
        * The "threshold" for a move to be considered is the `current_score`.
    * **b) Probabilistic Choice:**
        * **If `uphill_moves` is empty:** The algorithm is at a local maximum and is stuck. It terminates and returns the best state found.
        * **If `uphill_moves` is not empty:** A new `current_state` is chosen by selecting one of the assignments from `uphill_moves` **uniformly at random**. If there are $k$ options, each has a $1/k$ probability of being chosen.

4.  **Iteration:** Repeat from Step 2 until a solution is found (`current_score == m`) or a maximum number of iterations is reached.

---

## 4. Summary of Key Learnings 📝

* **Problem & Solution Fit:** 3-SAT's structure is well-suited for a local search where the goal is to maximize a score (satisfied clauses).
* **The "Stochastic" Advantage:** The randomness is not in evaluating moves but in **choosing which good move to make**. This allows the algorithm to explore different paths up the "search landscape" and reduces the chance of getting stuck in the same local maximum on every run.
* **Simplicity of Probability:** The probability is not a complex, tunable parameter. It's a natural consequence of the random selection from a list of valid options.
* **Local Maximum is a Risk:** Like all hill-climbing variants, this algorithm is **not guaranteed** to find the global optimum (a solution). It can terminate at a local maximum (an assignment that is not a solution but where no single flip can improve the score).