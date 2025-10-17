# The 8-Puzzle Problem

The **8-Puzzle** is a classic sliding puzzle consisting of a 3×3 grid with **8 numbered tiles (1–8)** and one **empty space**.  
The goal is to rearrange the tiles from a **random starting configuration** into a **goal configuration** by sliding tiles into the empty space.

---

## Key Concepts

- **State:** A specific arrangement of tiles on the board.  
- **Initial State:** The puzzle’s starting configuration.  
- **Goal State:** The desired final configuration.  
- **Actions/Moves:** Sliding a tile horizontally or vertically into the adjacent empty space.  
- **Solution:** A sequence of moves from the initial state to the goal state.  

The challenge: **Find the shortest sequence of moves** to reach the goal.

---

# A* Search Algorithm — The Smart Pathfinding Method

**A\*** (pronounced *A-star*) is an intelligent search algorithm for finding the **shortest path** between a start and a goal.  
It uses both **actual cost** and **estimated cost** to guide its search efficiently.

---

## The Core Formula

\[
f(n) = g(n) + h(n)
\]

Where:

| Term | Meaning |
|------|----------|
| **n** | A specific state (arrangement of puzzle tiles) |
| **g(n)** | Actual cost from the initial state to state *n* (number of moves so far) |
| **h(n)** | Heuristic estimate of the cost from *n* to the goal (remaining effort) |
| **f(n)** | Total estimated cost of the optimal path through *n* |

A\* always expands the node with the **lowest f(n)** first.

---

## The Heuristic: Manhattan Distance

The **Manhattan Distance** is the most effective heuristic for the 8-puzzle.

For each tile:
- Calculate how many horizontal and vertical moves it needs to reach its correct position.
- Ignore other tiles when calculating this.

\[
h(n) = \sum_{i=1}^{8} \text{(number of horizontal + vertical moves tile i is away from its goal position)}
\]

This heuristic is **admissible** — it never overestimates the true cost.  
✅ Therefore, **A\*** is guaranteed to find the **shortest possible solution**.

---

## How A* Works: Open and Closed Lists

- **Open List:**  
  Contains states discovered but not yet explored.  
  Implemented as a **priority queue**, always selecting the state with the **lowest f(n)**.

- **Closed List:**  
  Contains states that have already been explored,  
  preventing loops and redundant processing.

---

## Algorithm Steps

1. **Initialization**
   - Create the initial state node.
   - Compute `f(n) = g(n) + h(n)` (where `g(n)=0` and `h(n)` is Manhattan Distance).
   - Add the initial node to the **Open List**.

2. **Loop (while Open List is not empty)**
   - **a. Select Node:**  
     Remove the node with the **lowest f(n)** (call it `current_node`).

   - **b. Check for Goal:**  
     If `current_node` is the goal state → **solution found!**  
     Reconstruct the path by following parent links.

   - **c. Move to Closed List:**  
     Add `current_node` to the **Closed List**.

   - **d. Generate Neighbors:**  
     Create all valid new states by sliding the blank tile **up, down, left, or right**.

   - **e. Process Neighbors:**
     - Ignore neighbors already in the Closed List.
     - Compute:
       - `g(n)` = `current_node.g + 1`
       - `h(n)` = Manhattan Distance
     - If the neighbor is **not in Open List** or has a **lower new g(n)**:
       - Update its `f(n)` value.
       - Set its parent to `current_node`.
       - Add it to the **Open List**.

3. **No Solution**
   - If the Open List becomes empty before reaching the goal,  
     the puzzle is **unsolvable**.

---

## Summary

| Concept | Description |
|----------|--------------|
| **Algorithm Type** | Informed (Heuristic) Search |
| **Evaluation Function** | `f(n) = g(n) + h(n)` |
| **Heuristic Used** | Manhattan Distance |
| **Optimality** | Guaranteed (because the heuristic is admissible) |
| **Goal** | Find the shortest sequence of moves to reach the goal state |

---
