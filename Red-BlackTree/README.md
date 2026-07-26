# Red-Black Tree

## Overview

This repository contains a modern Python implementation of a **Red-Black Tree (RBT)**. While the underlying algorithms follow the implementation presented in the ZyBooks *Data Structures and Algorithms II* textbook, the code has been refactored to emphasize readability, maintainability, static type safety, and current Python best practices.

A red-black tree is a self-balancing binary search tree that uses node colors and structural rules to maintain logarithmic height during insertion and deletion.

## Features

- Red-black tree insertion with automatic balancing
- Red-black tree deletion with automatic rebalancing
- Left and right tree rotations
- Recursive search
- Tree height and node count operations
- ASCII tree visualization with node colors
- Modern Python type hints
- Google-style docstrings
- PEP 8 compliant formatting

## Project Structure

```text
.
├── main.py              # Demonstration program
├── rbt_node.py          # Red-black tree node implementation
├── rbt_print.py         # ASCII tree visualization
├── red_black_tree.py    # Red-black tree implementation
└── README.md
```

## Running the Example

From the project directory:

```bash
python main.py
```

The demonstration program:

1. Creates an empty red-black tree.
2. Inserts a predefined set of keys.
3. Displays the completed tree.
4. Removes several keys while maintaining the red-black tree properties.
5. Displays the tree after each successful removal.

Python 3.11 or newer is recommended.

## Concepts Demonstrated
- Red-black trees
- Self-balancing binary search trees
- Tree rotations
- Node-color invariants
- Binary search tree insertion
- Binary search tree deletion
- Recursive algorithms
- Object-oriented programming
- Enumerations
- Static type annotations

## Improvements over the Textbook Implementation

Compared to the original ZyBooks implementation, this version includes:

- Modern Python type annotations throughout
- Google-style docstrings
- Direct attribute access instead of trivial getter and setter methods
- `Enum`-based node colors instead of integer constants
- Simplified control flow and helper methods
- Improved naming consistency
- PEP 8 compliant formatting
- Additional assertions to improve static type analysis
- Cleaner project organization using snake_case module names
- A conventional `main()` entry point protected by `if __name__ == "__main__":`

## Acknowledgements

This project is based on the red-black tree algorithms presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithms.