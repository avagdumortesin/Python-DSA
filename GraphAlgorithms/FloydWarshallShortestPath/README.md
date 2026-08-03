# Floyd-Warshall All-Pairs Shortest Paths

## Overview

This project demonstrates an implementation the **Floyd-Warshall algorithm** in Python to compute the shortest path between every pair of vertices in a weighted directed graph. The algorithm iteratively considers each vertex as an intermediate waypoint, updating path lengths whenever a shorter route is discovered. 

The implementation is based on the example presented in the WGU zyBooks *Data Structures and Algorithms II* textbook. It has been refactored using modern Python features such as dataclasses, type annotations, comprehensions, and improved encapsulation, while preserving the original algorithm.

## Features

- Implements the Floyd-Warshall all-pairs shortest-path algorithm
- Supports weighted directed graphs with positive and negative edge weights
- Computes shortest-path distances between every pair of vertices
- Reconstructs the shortest path between any two connected vertices
- Weighted graph implementation using `Vertex` and `Edge` dataclasses
- Comprehensive type annotations and docstrings
- Pythonic collection comprehensions
- Demonstrates the algorithm using four sample graphs

## Project Structure

```text
.
├── graph.py
├── graph_components.py
├── shortest_path_matrix.py
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
All pairs shortest path matrix (graph 1):
     A   B   C   D 
A [  0   2  -1   9  ]
B [  2   0  -3   7  ]
C [  5   7   0   14 ]
D [ -4  -2  -5   0  ]
Shortest path from C to D:
C to A to B to D


All pairs shortest path matrix (graph 2):
     A   B   C   D 
A [  0   4   7   13 ]
B [  8   0   3   9  ]
C [  5   9   0   6  ]
D [ -1   3   6   0  ]
Shortest path from D to B:
D to A to B


All pairs shortest path matrix (graph 3):
     A   B   C 
A [  0   1  -7  ]
B [ inf  0  -8  ]
C [ inf inf  0  ]
Shortest path from C to A:
No path exists.

All pairs shortest path matrix (graph 4):
     A   B   C   D   E 
A [  0   1   3   6   8  ]
B [  0   0   2   5   8  ]
C [ -2  -1   0   3   6  ]
D [ -5  -4  -2   0   3  ]
E [  4   5   7   9   0  ]
Shortest path from A to D:
A to B to C to D
```

## Concepts Demonstrated

- Floyd-Warshall algorithm
- Dynamic programming
- All-pairs shortest paths
- Path reconstruction
- Weighted directed graphs
- Distance matrices
- Dataclasses
- Type annotations

## Improvements over the Textbook Implementation

- `@dataclass` implementations for `Vertex` and `Edge`
- Comprehensive type annotations
- Module, class, and method docstrings
- Dictionary comprehensions for matrix initialization
- Cleaner collection access using `.values()`
- `list()` construction instead of manual loops where appropriate
- Generator expressions with `any()`
- Improved helper methods and separation of responsibilities
- PEP 8-compliant formatting and naming conventions

## Acknowledgements

This project is based on Floyd-Warshall all-pairs shortest-path algorithm presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithm.