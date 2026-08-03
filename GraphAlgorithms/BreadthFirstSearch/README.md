# Breadth-First Search (BFS)

## Overview

This project demonstrates an iterative implementation of the **Breadth-First Search (BFS)** graph traversal algorithm in Python. The implementation is based on the BFS example presented in the WGU zyBooks *Data Structures and Algorithms II* textbook, but has been refactored into a modern, type-safe, object-oriented Python implementation.

Breadth-first search explores a graph level by level, visiting all neighboring vertices before proceeding to the next depth. This implementation uses a queue to manage traversal order and employs the Visitor design pattern to separate traversal logic from vertex processing.

## Features

- Iterative breadth-first traversal using a queue
- Support for directed and undirected graphs
- Visitor pattern for customizable vertex processing
- Dataclass-based graph components with `slots=True`
- Fully type-annotated implementation
- Comprehensive documentation through module, class, and method docstrings
- Demonstration using three sample graphs

## Project Structure

```text
.
├── bfs_visitors.py
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
Breadth-first search traversal
Start vertex: Eva
Eva: 0
Joe: 1
Lily: 1
Taj: 2
Jun: 2
Chen: 3
Ken: 3
```

## Concepts Demonstrated

- Breadth-First Search (BFS)
- Graph traversal using a queue
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

This project is based on the breadth-first search algorithms presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithm.