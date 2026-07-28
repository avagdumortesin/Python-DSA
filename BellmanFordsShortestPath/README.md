# Bellman-Ford Shortest Path Algorithm

## Overview

This project demonstrates an implementation of the **Bellman-Ford Shortest Path Algorithm** in Python. The implementation is based on the example presented in the WGU zyBooks *Data Structures and Algorithms II* textbook but has been refactored using modern Python features while preserving the original algorithm.

Bellman-Ford computes the minimum total path weight from a starting vertex to every reachable vertex in a weighted graph, even when negative edge weights are present. Unlike Dijkstra's algorithm, Bellman-Ford can also detect reachable negative-weight cycles, which indicate that no shortest path exists.

## Features

- Single-source shortest path computation
- Support for weighted directed and undirected graphs
- Support for negative edge weights
- Detection of reachable negative-weight cycles
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

A to B: A -> B (total weight: 1)

A to C: A -> C (total weight: 2)

A to D: A -> B -> D (total weight: 4)

A to E: A -> B -> E (total weight: 3)

A to F: A -> B -> E -> F (total weight: 6)

```

## Concepts Demonstrated

- Bellman-Ford shortest path algorithm
- Weighted graph representations
- Directed and undirected graphs
- Negative edge weights
- Negative-weight cycle detection
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
- Added an early-exit optimization when no edge relaxations occur during an iteration.
- Simplified edge relaxation by iterating directly over all graph edges.
- Added complete type annotations throughout the project.
- Added module, class, and method docstrings.
- Improved readability through descriptive variable names.
- Added validation for unreachable paths during path reconstruction.
- Improved readability through PEP 8 formatting.
- Organized the project using snake_case module names.

## Acknowledgements

This project is based on the Bellman-Ford shortest path algorithm presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithm.