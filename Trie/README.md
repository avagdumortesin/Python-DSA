# Trie

## Overview

This repository contains a modern Python implementation of a **trie**, also known as a **prefix tree**. While the underlying algorithms follow the implementation presented in the ZyBooks *Data Structures and Algorithms II* textbook, the code has been refactored to emphasize readability, maintainability, static type safety, and current Python best practices.

A trie stores strings one character at a time along shared paths. This structure supports efficient insertion, exact-string lookup, and removal without storing each word as an independent value.

## Features

- Insert strings into the trie
- Search for complete strings
- Test whether a string is present
- Report the number of nodes visited during a search
- Remove stored strings recursively
- Remove unused branches after deletion
- Distinguish complete strings from shared prefixes with a terminal marker
- Modern Python type annotations
- Comprehensive docstrings
- PEP 8 compliant naming and formatting

## Project Structure

```text
.
├── trie.py
├── trie_node.py
├── main.py
└── README.md
```

## Running the Project

Run the demonstration from the project directory:

```bash
python main.py
```

Python 3.12 or newer is required because the implementation uses the modern `type` statement for the `SearchResult` alias.

Example Output:

```text
Inserting "CAT"
Inserting "DOG"
Inserting "BIRD"
Inserting "FISH"
Inserting "HAMSTER"
Inserting "SNAKE"
Search for "CAT" returned True and visited 4 nodes
Search for "BAT" returned False and visited 1 node
Search for "RAT" returned False and visited 0 nodes
Search for "HIPPOPOTAMUS" returned False and visited 1 node
Search for "HAMSTER" returned True and visited 8 nodes
Search for "FERRET" returned False and visited 1 node
Search for "OCTOPUS" returned False and visited 0 nodes
```

The node count includes the terminal-marker node for successful searches but does not include the root node.

## Concepts Demonstrated

- Trie and prefix-tree data structures
- Character-by-character string storage
- Shared-prefix representation
- Dictionary-based child-node lookup
- Recursive deletion
- Tree pruning
- Terminal markers
- Type aliases
- Object-oriented programming
- Static type annotations

## Improvements over the Textbook Implementation

- Modern Python type annotations throughout
- A named `SearchResult` type alias for search return values
- Forward-reference support through `from __future__ import annotations`
- A named `_TERMINAL_MARKER` constant instead of repeated null-character literals
- Comprehensive class and method docstrings
- PEP 8 naming conventions and snake_case module names
- Use of `is None` and `is not None` for identity comparisons
- Simplified child lookup through `dict.get()`
- Renaming `add_new_child()` to the more concise `add_child()`
- A private `_remove_recursive()` helper to distinguish internal implementation details from the public API
- Safer branch pruning that removes a child only when the requested string was successfully removed and the child has no remaining descendants
- Explicit return types for insertion, lookup, removal, and node-management operations

## Acknowledgements

This project is based on the trie algorithms presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithms.
