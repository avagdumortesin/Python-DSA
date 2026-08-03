# Minimum Spanning Tree

## Overview

This project demonstrates an implementation of **Kruskal's Minimum Spanning Tree Algorithm** in Python. The implementation is based on the example presented in the WGU zyBooks *Data Structures and Algorithms II* textbook but has been refactored using modern Python features while preserving the original algorithm.

Given a connected, weighted graph, the algorithm constructs a minimum spanning tree (MST) by repeatedly selecting the lowest-weight edge that does not create a cycle.

## Features

- Kruskal's Minimum Spanning Tree algorithm
- Weighted graph implementation using `Vertex` and `Edge` dataclasses
- Automatic cycle prevention through a vertex set collection
- Type annotations throughout
- Comprehensive docstrings
- Pythonic collection comprehensions
- Demonstration using two sample graphs

## Project Structure

```text
.
├── graph.py
├── graph_components.py
├── vertex_set_collection.py
├── main.py
└── README.md
```

## Running the Example

Run the demonstration from the project directory:

```bash
python main.py
```

Example output:

```text
Edges in minimum spanning tree (graph 1):
  D -- A, weight = 6
  E -- D, weight = 8
  C -- B, weight = 9
  B -- H, weight = 10
  D -- B, weight = 12
  G -- B, weight = 14
  F -- E, weight = 20

Edges in minimum spanning tree (graph 2):
  D -- B, weight = 60
  F -- E, weight = 70
  G -- F, weight = 72
  E -- D, weight = 80
  B -- A, weight = 80
  C -- B, weight = 90
  P -- B, weight = 100
```

## Concepts Demonstrated

- Kruskal's Minimum Spanning Tree algorithm
- Weighted graph representations
- Cycle detection in graph algorithms
- Greedy algorithms
- Disjoint-set (vertex set) collections
- Graph traversal
- Dataclasses
- Type annotations

## Improvements over the Textbook Implementation

- `@dataclass` implementations for `Vertex` and `Edge`
- Comprehensive type annotations
- Module, class, and method docstrings
- Dictionary and set comprehensions
- Cleaner collection access using `.values()`
- `list()` construction instead of manual loops where appropriate
- Generator expressions with `any()`
- `sorted()` replacing `queue.PriorityQueue` while maintaining the same **O(E log E)** time complexity
- Encapsulation of merge validation within `VertexSetCollection`
- PEP 8-compliant formatting and naming conventions

## Acknowledgements

This project is based on the Kruskal's Minimum Spanning Tree algorithm presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithm.