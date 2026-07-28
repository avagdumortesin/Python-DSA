# Topological Sort

## Overview

This project demonstrates an implementation of **Kahn's Topological Sorting Algorithm** in Python. The implementation is based on the example presented in the WGU zyBooks *Data Structures and Algorithms II* textbook but has been refactored using modern Python features while preserving the original algorithm.

Topological sorting produces a linear ordering of the vertices in a directed acyclic graph (DAG) such that every directed edge points from an earlier vertex in the ordering to a later one. This implementation uses Kahn's algorithm, which repeatedly removes vertices with no incoming edges until all vertices have been processed or a cycle is detected.

## Features

- Topological sorting of directed acyclic graphs (DAGs)
- Automatic cycle detection for invalid graphs
- Support for directed and undirected graph construction
- Dataclass-based graph components
- Fully type-annotated implementation
- Comprehensive documentation through module, class, and method docstrings
- Demonstration using two sample graphs

## Project Structure

```text
.
├── graph.py
├── graph_components.py
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
Graph 1: E, A, C, D, B, F, G
Graph 2: D, B, C, F, A, E, G
```

*Note:* A directed acyclic graph may have multiple valid topological orderings. Your output may differ from the example while still being correct.

## Concepts Demonstrated

- Kahn's topological sorting algorithm
- Directed acyclic graphs (DAGs)
- Directed graph representations
- In-degree counting
- Cycle detection
- Object-oriented design
- Python dataclasses
- Type annotations and modern Python development practices

## Improvements over the Textbook Implementation

- Replaced manual graph component classes with `@dataclass` models.
- Added `slots=True` to reduce instance overhead.
- Preserved identity-based graph semantics using `eq=False`.
- Added `Vertex.__str__()` to encapsulate vertex display.
- Replaced manual incoming-edge counting with a dictionary comprehension.
- Replaced manual initialization of zero in-degree vertices with a list comprehension.
- Added complete type annotations throughout the project.
- Added module, class, and method docstrings.
- Added validation that raises a `ValueError` when the graph contains a cycle.
- Improved readability through descriptive variable names.
- Improved readability through PEP 8 formatting.
- Organized the project using snake_case module names.

## Acknowledgements

This project is based on the topological sorting algorithm presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithm.