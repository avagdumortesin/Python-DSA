# Breadth-First Search (BFS)

## Overview

This project implements the **Breadth-First Search (BFS)** graph traversal algorithm in Python. It demonstrates how BFS explores a graph level-by-level using a queue while computing the minimum number of edges (hop count) from a starting vertex to every reachable vertex.

The implementation is based on the example presented in the ZyBooks
*Data Structures and Algorithms* textbook, but has been refactored into a modern, type-safe, object-oriented Python implementation.

## Features

-   Directed and undirected graph support
-   Breadth-first graph traversal
-   Visitor pattern for traversal processing
-   Distance calculation from the starting vertex
-   Modern Python type hints
-   Dataclasses with `slots=True`
-   Abstract base class for the visitor interface
-   Comprehensive docstrings
-   PEP 8 compliant formatting

## Project Structure

``` text
.
├── bfs_visitors.py
├── graph.py
├── graph_components.py
├── main.py
└── README.md
```

## Example Output

``` text
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

-   Graph data structures
-   Adjacency lists
-   Breadth-First Search (BFS)
-   Queue-based graph traversal
-   Visitor design pattern
-   Object-oriented programming
-   Python dataclasses
-   Type annotations
-   Abstract base classes

## Improvements over the Textbook Implementation

Compared to the original textbook implementation, this project includes:

-   Modern Python type annotations throughout
-   Dataclasses for `Vertex` and `Edge`
-   An abstract base class for the visitor interface
-   Improved naming conventions following PEP 8
-   Comprehensive module, class, and method documentation
-   A conventional `main()` entry point
-   Strongly typed collections
-   Use of `collections.deque` instead of `queue.Queue` for BFS
    traversal
-   Modernized project structure and organization

## Running the Project

From the project directory:

``` bash
python main.py
```

Python 3.11 or newer is recommended.
