# AVL Tree

## Overview

This project demonstrates a Python implementation of an **AVL Tree**, a self-balancing binary search tree that automatically maintains its height by performing rotations after insertions and deletions. While the underlying algorithms follow the implementation presented in the WGU zyBooks *Data Structures and Algorithms II* textbook, the code has been refactored to emphasize readability, maintainability, static type safety, and current Python best practices.

AVL Trees ensure that the heights of the left and right subtrees of every node differ by at most one. This balance guarantee provides logarithmic-time search, insertion, and deletion operations while minimizing tree height.

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
├── avl_tree.py
├── avl_tree_node.py
├── main.py
└── README.md
```

## Running the Example

Run the demonstration from the project directory:

```bash
python main.py
```

The demonstration program:

1. Creates an empty AVL tree.
2. Inserts a predefined set of keys.
3. Displays the completed tree.
4. Removes several keys while maintaining the AVL tree properties.
5. Displays the tree after each successful removal.

Example output:

```text
Tree after initial insertions:
          ___[15]____
         /           \
      [10]           [20]
     /    \         /    \
   [5]    [12]   [19]    [22]
  /             /            \
[3]          [18]            [47]

Removed key 12:
      ___[15]____
     /           \
   [5]           [20]
  /   \         /    \
[3]   [10]   [19]    [22]
            /            \
         [18]            [47]

Removed key 20:
      ___[15]____
     /           \
   [5]           [22]
  /   \         /    \
[3]   [10]   [19]    [47]
            /
         [18]

Failed to remove key 30 (not found)
```

> **Note:** The exact output depends on the demonstration sequence used in `main.py`, but it illustrates the tree maintaining AVL balance through the appropriate rotations after insertions and deletions.

## Concepts Demonstrated

- AVL Trees
- Self-balancing binary search trees
- Single and double tree rotations
- Balance factors and height calculations
- Binary search tree insertion and deletion
- Object-oriented programming
- Type annotations and modern Python development practices

## Improvements over the Textbook Implementation

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

## Acknowledgements

This project is based on the AVL Tree algorithms presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithms.