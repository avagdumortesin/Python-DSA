# Red-Black Tree

## Overview

This project demonstrates a Python implementation of a **Red-Black Tree**, a self-balancing binary search tree that maintains logarithmic-time insertion, deletion, and lookup operations through a series of color and rotation rules. While the underlying algorithms follow the implementation presented in the WGU zyBooks *Data Structures and Algorithms II* textbook, the code has been refactored to emphasize readability, maintainability, static type safety, and current Python best practices.

Red-Black Trees automatically maintain balance after insertions and deletions by enforcing a set of structural properties. These rules ensure that no path through the tree becomes significantly longer than another, providing efficient performance without requiring complete rebalancing after every modification.

## Features

- Red-black tree insertion and deletion with automatic rebalancing
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
├── red_black_tree.py
├── rb_tree_node.py
├── main.py
└── README.md
```

## Running the Example

Run the demonstration from the project directory:

```bash
python main.py
```

The demonstration program:

1. Creates an empty red-black tree.
2. Inserts a predefined set of keys.
3. Displays the completed tree.
4. Removes several keys while maintaining the red-black tree properties.
5. Displays the tree after each successful removal.

Example output:

```text
Tree after initial insertions:
                ____[15 B]_____
               /               \
          [10 R]               [20 R]
         /      \             /      \
     [5 B]      [12 B]   [19 B]      [22 B]
    /                   /                  \
[3 R]              [18 R]                  [47 R]


Tree after removing 12:
          ____[15 B]_____
         /               \
     [5 R]               [20 R]
    /     \             /      \
[3 B]     [10 B]   [19 B]      [22 B]
                  /                  \
             [18 R]                  [47 R]

Tree after removing 20:
          ____[15 B]_____
         /               \
     [5 R]               [22 R]
    /     \             /      \
[3 B]     [10 B]   [19 B]      [47 B]
                  /
             [18 R]

Failed to remove key 30 (not found)
```

> **Note:** The exact output depends on the demonstration sequence used in `main.py`, but it illustrates the tree maintaining Red-Black properties throughout insertions and deletions.

## Concepts Demonstrated

- Red-Black Trees
- Self-balancing binary search trees
- Tree rotations
- Tree recoloring
- Binary search tree insertion and deletion
- Recursive algorithms
- Object-oriented programming
- Enumerations
- Type annotations and modern Python development practices

## Improvements over the Textbook Implementation

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

This project is based on the Red-Black Tree algorithms presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithms.