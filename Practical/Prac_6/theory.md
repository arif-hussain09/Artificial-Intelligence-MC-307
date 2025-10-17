# Understanding AND-OR Graphs with Example

An **AND-OR graph** represents problems that can be divided into smaller subproblems, combining both **choices (OR)** and **requirements (AND)**.


---

## Explanation

### (a) Basic AND-OR Graph
- Shows relationships between nodes using **directed edges**.  
- **Numbers on edges** represent **costs** or **weights**.  
- **Arrows** indicate dependencies between parent and child nodes.

### (b) Expanded AND-OR Graph with Costs
- Displays **combined node labels** (e.g., `2-3`, `3-4`) representing multiple subproblems.  
- The **numbers beside edges** show **cost values** used in the **AO\*** algorithm for computing optimal paths.

---

## In Context: AO* Algorithm
When applied to this type of graph:
- **OR nodes** allow selecting the least-cost child.
- **AND nodes** require solving **all connected children**.
- AO* iteratively updates the **cost estimates** and identifies the **minimum-cost solution subgraph**.

This diagram illustrates how the algorithm processes multiple possible paths and merges both **AND** and **OR** relationships efficiently.
