# Red-Black Tree

A Python implementation of a **Red-Black Tree (RBT)** based on the binary search tree algorithms presented in *Data Structures and Algorithms II*. This version modernizes the original educational implementation while preserving the underlying algorithms and balancing logic.

## Features

- Red-black tree insertion with automatic balancing
- Red-black tree deletion with automatic rebalancing
- Left and right tree rotations
- Recursive search
- Tree height and node count operations
- ASCII tree visualization with node colors
- Type hints throughout
- Google-style docstrings
- Modern Python coding practices

## Project Structure

```
.
├── main.py              # Demonstration program
├── rbt_node.py          # Red-black tree node implementation
├── rbt_print.py         # ASCII tree visualization
├── red_black_tree.py    # Red-black tree implementation
└── README.md
```

## Running the Example

Run the demonstration program:

```bash
python main.py
```

The example program:

1. Creates an empty red-black tree.
2. Inserts a predefined set of keys.
3. Displays the completed tree.
4. Removes several keys while maintaining the red-black tree properties.
5. Displays the tree after each successful removal.

## Modernization Notes

Compared to the original textbook implementation, this version includes:

- Modern Python type annotations
- Google-style docstrings
- Direct attribute access instead of trivial getter/setter methods
- `Enum`-based node colors instead of integer constants
- Simplified control flow and helper methods
- Improved naming consistency
- Ruff-formatted source code
- Additional assertions to improve static type analysis

## Acknowledgements

This project is based on the red-black tree algorithms presented in:

> Lysecky, R., & Vahid, F. (2018, June). _C950: Data Structures and Algorithms II_. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithms.