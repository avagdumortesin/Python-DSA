# AVL Tree

## Overview

This repository contains a modern Python implementation of an **AVL tree**, a self-balancing binary search tree that automatically maintains logarithmic height through rotations after insertions and deletions. While the underlying algorithms follow the implementation presented in the ZyBooks *Data Structures and Algorithms II* textbook, the code has been refactored to emphasize readability, maintainability, static type safety, and current Python best practices.

By maintaining a balance factor for every node, an AVL tree guarantees efficient search, insertion, and deletion operations while avoiding the performance degradation that can occur in an unbalanced binary search tree.

## Features

- Self-balancing binary search tree
- Automatic left and right rotations
- Double-rotation support (Left-Right and Right-Left)
- Insertion and deletion with rebalancing
- Height maintenance
- Balance-factor calculation
- Parent node references
- ASCII tree visualization
- Modern Python type annotations
- Comprehensive docstrings
- PEP 8 compliant formatting

## Project Structure

```text
.
├── avl_node.py
├── avl_print.py
├── avl_tree.py
├── main.py
└── README.md
```

## Example Output

```text
Tree after initial insertions:
<ASCII tree output>

Removed key 12:
<updated tree>

Removed key 20:
<updated tree>

Failed to remove key 30 (not found)
```

## Concepts Demonstrated

- AVL trees
- Self-balancing binary search trees
- Tree rotations
- Recursive height maintenance
- Balance factors
- Binary search tree deletion
- Object-oriented programming
- Static type annotations

## Improvements over the Textbook Implementation

Compared to the original ZyBooks implementation, this project includes:

- Modern Python type annotations throughout
- Comprehensive module, class, and method docstrings
- Forward-reference support through `from __future__ import annotations`
- PEP 8 naming conventions and snake_case module names
- A conventional `main()` entry point protected by `if __name__ == "__main__":`
- Stronger `None` handling using optional types
- Improved helper method naming through private implementation methods
- Cleaner rotation and rebalancing logic
- More descriptive parameter and variable names
- Improved readability and maintainability while preserving the original AVL algorithms

## Running the Project

From the project directory:

```bash
python main.py
```

Python 3.11 or newer is recommended.

## Acknowledgements

This project is based on the AVL tree algorithms presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithms.
