# Binary Search Tree

## Overview

This repository contains a modern Python implementation of a **Binary Search Tree (BST)**. While the underlying algorithms follow the implementation presented in the ZyBooks *Data Structures and Algorithms II* textbook, the code has been refactored to emphasize readability, maintainability, static type safety, and modern Python best practices.

The implementation supports insertion, searching, deletion, height calculation, and ASCII visualization of the tree structure.

## Features

-   Binary search tree insertion
-   Search and membership testing
-   Node removal
-   Tree height calculation
-   Parent node references
-   ASCII tree visualization
-   Modern Python type hints
-   Comprehensive docstrings
-   PEP 8 compliant formatting

## Project Structure

``` text
.
├── binary_search_tree.py
├── bst_node.py
├── bst_print.py
├── main.py
└── README.md
```

## Example Output

``` text
Initial tree:
<ASCII tree output>

Tree after removing 5:
<updated tree>

Tree after removing 3:
<updated tree>
```

## Concepts Demonstrated

-   Binary search trees
-   Recursive algorithms
-   Tree insertion
-   Tree deletion
-   Tree traversal
-   Parent-child relationships
-   Object-oriented programming
-   Type annotations

## Improvements over the Textbook Implementation

Compared to the original ZyBooks implementation, this project includes:

-   Modern Python type annotations throughout
-   Comprehensive module, class, and method docstrings
-   PEP 8 naming conventions
-   Cleaner project organization using snake_case module names
-   A conventional `main()` entry point protected by
    `if __name__ == "__main__":`
-   Improved parameter naming for readability
-   Better encapsulation through helper methods
-   Stronger `None` handling with optional types
-   More maintainable ASCII tree-printing utilities

## Running the Project

From the project directory:

``` bash
python main.py
```

Python 3.11 or newer is recommended.

## Acknowledgements

This project is based on the binary search tree algorithms presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithms.
