# Design Decisions – Circular Dependency Detection

## Approach
Tasks and dependencies are modeled as a directed graph where:
- Each task is a node
- Each dependency is a directed edge

When adding a new dependency, a **Depth First Search (DFS)** is executed from the dependent task to detect if the source task is reachable again.

If a path exists, a circular dependency is detected and rejected.

---

## Algorithm Used
- Depth First Search (DFS)
- Recursion stack tracking

---

## Time Complexity
- O(V + E)
Where:
- V = number of tasks
- E = number of dependencies

---

## Reason for Choice
DFS allows:
- Efficient cycle detection
- Path reconstruction for meaningful error messages
- Simple implementation and readability
