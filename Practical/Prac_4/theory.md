# Solving the Puzzle with Hill Climbing

## Why Not Brute Force?
A brute-force approach (trying every possible combination) is too slow.  
Instead, we use a **guided search** method — **Hill Climbing**.

---

## The Analogy
Imagine you're on a **foggy mountain** trying to reach the **highest peak**.  
You can only see your immediate surroundings, so you always take a step **uphill** until every nearby step is **downhill**.

---

## Translating to the 3-SAT Problem

| Concept | Hill Climbing Analogy | 3-SAT Equivalent |
|----------|------------------------|------------------|
| **Position on the Hill** | Current location | A TRUE/FALSE assignment for all variables (e.g., x₁=T, x₂=F, x₃=F, x₄=T) |
| **Height/Altitude** | Elevation | Number of satisfied clauses (objective function) |
| **Peak** | Highest point | All clauses are satisfied (solution found) |
| **Move** | Step in some direction | Flip one variable (e.g., x₁ from TRUE → FALSE) |

---

## The Problem: Local Optima
A **local optimum** is a small peak — all nearby moves make things worse, but it's **not the global peak** (true solution).  
The basic Hill Climbing algorithm can get stuck here.

---

## The Improvement: Stochastic Hill Climbing
To escape local optima, introduce **randomness**:
- Instead of always picking the *best* uphill move, randomly pick **any** uphill move.
- This allows exploration of different "mountain paths" toward the true peak.

---

## Algorithm Steps

1. **Start**  
   Generate a random TRUE/FALSE assignment for all variables.

2. **Evaluate**  
   Compute the score = number of satisfied clauses.

3. **Check for Solution**  
   If `score == total_clauses`, we found a solution → **Stop**.

4. **Find Neighbors**  
   Generate all neighboring states by flipping one variable at a time.

5. **Identify Uphill Moves**  
   Select only neighbors with a higher score than the current one.

6. **Make a Move**  
   - If no uphill moves → local optimum reached → **random restart** (go back to Step 1).  
   - If uphill moves exist → randomly choose one and move to it.

7. **Repeat**  
   Continue Steps 2–6 until a solution is found or attempts run out.

---

## Mathematical Intuition

Let:

- **F** = 3-CNF formula with *n* variables and *m* clauses.  
- **S** = a truth assignment `{v₁, v₂, ..., vₙ}`, where `vᵢ ∈ {TRUE, FALSE}`.  
- **f(S)** = number of clauses satisfied by `S`.

Goal:
\[
\text{Find } S^* \text{ such that } f(S^*) = m
\]

Neighbor:
\[
S' = \text{assignment obtained by flipping one variable in } S
\]

Uphill neighbors:
\[
U(S) = \{ S' \mid f(S') > f(S) \}
\]

Transition rule:
\[
S_{\text{next}} = \text{randomly chosen element from } U(S)
\]

If \( U(S) = \emptyset \), perform a **random restart**.

---

**Result:**  
Stochastic Hill Climbing combines **directed search** (always improving) with **randomness** (escaping traps), making it an effective method for solving complex optimization problems like **3-SAT**.
