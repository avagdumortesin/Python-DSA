# Dijkstra's Shortest Path Algorithm

## Overview

This project demonstrates an implementation of **Dijkstra's Shortest Path Algorithm** in Python. The implementation is based on the example presented in the WGU zyBooks *Data Structures and Algorithms II* textbook but has been refactored using modern Python features while preserving the original algorithm.

Dijkstra's algorithm computes the minimum total path weight from a starting vertex to every reachable vertex in a weighted graph with non-negative edge weights. This implementation records predecessor vertices during traversal, allowing the shortest path to any reachable destination to be reconstructed after the algorithm completes.

## Features

- Single-source shortest path computation
- Support for weighted directed and undirected graphs
- Automatic shortest-path reconstruction
- Dataclass-based graph components
- Fully type-annotated implementation
- Comprehensive documentation through module, class, and method docstrings
- Demonstration using a sample weighted graph

## Project Structure

```text
.
├── graph.py
├── graph_components.py
├── main.py
├── path_vertex_info.py
└── README.md
```

## Running the Example

Run the demonstration from the project directory:

```bash
python main.py
```

Example output:

```text
A to A: A (total weight: 0)

A to B: A -> B (total weight: 8)

A to C: A -> D -> C (total weight: 4)

A to D: A -> D (total weight: 3)

A to E: A -> D -> C -> E (total weight: 6)

A to F: A -> D -> C -> E -> F (total weight: 10)

A to G: A -> D -> C -> E -> F -> G (total weight: 11)

```

## Concepts Demonstrated

- Dijkstra's shortest path algorithm
- Greedy algorithms
- Weighted graph representations
- Directed and undirected graphs
- Path reconstruction using predecessor links
- Object-oriented design
- Python dataclasses
- Type annotations and modern Python development practices

## Improvements over the Textbook Implementation

- Replaced manual graph component classes with `@dataclass` models.
- Added `slots=True` to reduce instance overhead.
- Preserved identity-based graph semantics using `eq=False`.
- Added `Vertex.__str__()` to encapsulate vertex display.
- Refactored vertex initialization using a dictionary comprehension.
- Eliminated duplicate object creation by deriving the unvisited list from the dictionary values.
- Added complete type annotations throughout the project.
- Added module, class, and method docstrings.
- Improved readability through descriptive variable names.
- Added validation for unreachable paths during path reconstruction.
- Improved readability through PEP 8 formatting.
- Organized the project using snake_case module names.

## Acknowledgements

This project is based on the Dijkstra's shortest path algorithm presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithm.