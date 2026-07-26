# Binary Search Tree Traversal

## Overview

This repository demonstrates the Visitor design pattern applied to binary search tree traversal. While the traversal algorithm originates from the ZyBooks *Data Structures and Algorithms II* textbook, the implementation has been modernized to improve readability, maintainability, static type safety, and adherence to current Python best practices.

Rather than embedding traversal behavior directly into the tree, the project delegates processing to interchangeable visitor objects. This separation of concerns makes it easy to extend traversal behavior without modifying the tree implementation.

## Features

-   Binary search tree implementation
-   In-order tree traversal
-   Visitor pattern implementation
-   Multiple visitor implementations
    -   PrintVisitor
    -   CountVisitor
    -   ListVisitor
-   Parent node references
-   Modern Python type hints
-   Protocol-based visitor interface
-   Comprehensive docstrings
-   PEP 8 compliant formatting

## Project Structure

``` text
.
├── binary_search_tree.py
├── bst_node.py
├── bst_node_visitor.py
├── print_visitor.py
├── count_visitor.py
├── list_visitor.py
├── main.py
└── README.md
```

## Example Output

``` text
12 19 23 25 26 44 54 67 73 76 81 83 88
PrintVisitor is done visiting nodes.

CountVisitor visited 13 nodes.

ListVisitor visited 13 nodes: 12 19 23 25 26 44 54 67 73 76 81 83 88
```

## Concepts Demonstrated

-   Binary search trees
-   In-order traversal
-   Visitor design pattern
-   Protocols
-   Object-oriented programming
-   Separation of concerns
-   Type annotations
-   Recursive algorithms

## Improvements over the Textbook Implementation

Compared to the original ZyBooks implementation, this project includes:

-   Modern Python type annotations throughout
-   A `main()` entry point guarded by `if __name__ == "__main__":`
-   Descriptive module, class, and method docstrings
-   PEP 8 naming conventions
-   Protocol-based visitor interface instead of an empty base class
-   Strongly typed visitor methods
-   Parent references stored within tree nodes
-   Improved helper method naming using private methods
-   Cleaner project organization using snake_case module names
-   Consistent formatting and readability improvements

## Running the Project

From the project directory:

``` bash
python main.py
```

Python 3.11 or newer is recommended.

## Acknowledgements

This project is based on the binary search tree traversal algorithms presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithms.
