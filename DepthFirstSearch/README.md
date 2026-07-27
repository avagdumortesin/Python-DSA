# Depth-First Search (DFS)

## Overview

This project demonstrates an iterative implementation of the **Depth-First Search (DFS)** graph traversal algorithm in Python. The implementation is based on the DFS example presented in the WGU zyBooks *Data Structures and Algorithms II* textbook but has been refactored using modern Python features while preserving the original traversal algorithm.

Depth-first search explores a graph by following each branch as deeply as possible before backtracking. This implementation uses an explicit stack rather than recursion and employs the Visitor design pattern to separate traversal logic from vertex processing.

## Features

- Iterative depth-first traversal using an explicit stack
- Support for directed and undirected graphs
- Visitor pattern for customizable vertex processing
- Dataclass-based graph components
- Fully type-annotated implementation
- Comprehensive documentation through module, class, and method docstrings
- Demonstration using three sample graphs

## Project Structure

```text
.
├── dfs_visitors.py
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
Depth-first search traversal
Graph 1: A D B F E C
Graph 2: A B C F E D
Graph 3: A E F D C B
```

## Concepts Demonstrated

- Depth-First Search (DFS)
- Graph traversal using a stack
- Directed and undirected graph representations
- Visitor design pattern
- Object-oriented design
- Python dataclasses
- Abstract Base Classes (ABC)
- Type annotations and modern Python development practices

## Improvements over the Textbook Implementation

- Replaced manual graph component classes with `@dataclass` models.
- Added `slots=True` to reduce instance overhead.
- Preserved identity-based graph semantics using `eq=False`.
- Added `Vertex.__str__()` to encapsulate vertex display.
- Replaced the informal visitor interface with an Abstract Base Class.
- Added complete type annotations throughout the project.
- Added module, class, and method docstrings.
- Introduced a reusable graph-construction helper function.
- Eliminated repeated optional vertex lookups by retaining references to created vertices.
- Replaced index-based iteration with `enumerate()`.
- Improved readability through descriptive naming and PEP 8 formatting.
- Organized the project using snake_case module names.

## Acknowledgements

This project is based on the depth-first search algorithms presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms
II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithm.