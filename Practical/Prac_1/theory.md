# The 8-Puzzle Problem: Search and Solvability

The **8-Puzzle** is a classic problem used to illustrate fundamental concepts in Artificial Intelligence search algorithms.  
It involves transforming an **Initial State** into a predefined **Goal State** by sliding the blank tile (`0`) into adjacent spaces.

---

## I. Problem Definition and State Representation

| **Component** | **Description** |
|----------------|-----------------|
| **Initial State** | The configuration of the 8 numbered tiles and the blank space. |
| **Goal State** | The desired solved configuration (e.g., tiles 1 through 8 in order). |
| **Operators** | Moving the blank tile (Up, Down, Left, Right) to generate valid neighboring states (NBD). |

---

## II. Search Strategy: Generate and Test (Uninformed Search)

Your pseudocode outlines a basic **uninformed search algorithm** (e.g., BFS, DFS) that systematically explores the state space.

### Search Components

| **Search Component** | **Data Structure Used** | **Purpose** |
|-----------------------|--------------------------|-------------|
| **Open Set (Frontier)** | `Open` (Queue or Priority Queue) | Stores neighboring nodes (states) that have been generated but not yet expanded. |
| **Closed Set (Visited)** | `Close` (Hash Set or Dictionary) | Stores all nodes already visited to prevent cycles and redundancy. |

### Pseudocode Analysis

The core **while loop** of any graph search:

1. **Selection:** Pick a node `n` from the open set.  
   - (The picking rule determines search type: FIFO → BFS, LIFO → DFS, Priority → A*.)
2. **Goal Check:**  
   ```if (n == goal) return True```
3. **Expansion:** Generate neighbors of node `n`.
4. **Update Rule:**  
