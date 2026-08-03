# Hash Table with Separate Chaining

## Overview

This project demonstrates a Python implementation of a **hash table using separate chaining** to resolve collisions. The implementation is based on the example presented in the WGU zyBooks *Data Structures and Algorithms II* textbook but has been refactored using modern Python features while preserving the original algorithm.

Separate chaining stores colliding entries in linked lists associated with each bucket of the hash table. This implementation supports insertion, lookup, removal, containment checks, and formatted display of both the table contents and the underlying bucket structure. It shares common map and hash table abstractions with the other collision-resolution strategies in this repository, allowing each implementation to focus only on its collision-resolution strategy.

## Features

- Hash table implementation using separate chaining
- Collision resolution using linked lists
- Fully type-annotated implementation
- Shared `MapADT` and `HashTable` framework with algorithm-specific collision handling
- Comprehensive documentation through module, class, and method docstrings
- Demonstration of insertion, removal, and bucket visualization

## Project Structure

```text
HashTableAlgorithms/
├── Chaining/
│   ├── chaining_hash_table.py
│   ├── main.py
│   └── README.md
└── shared/
    ├── __init__.py
    ├── hash_table.py
    ├── map_adt.py
    └── README.md
```

## Shared Components

This implementation uses the common `MapADT` and `HashTable` abstractions
located in `HashTableAlgorithms/shared`.

Unlike the open-addressing implementations, chaining does not use
`OpenAddressingBucket`; each bucket stores the head of a linked list.

See the [`shared` README](../shared/README.md) for additional details.

## Running the Example

Run the demonstration from the project directory:

```bash
python main.py
```

Example output (bucket assignments will vary because Python randomizes string hashes between interpreter sessions):

```text
Items: 
LAX: Los Angeles
SFO: San Francisco
IAH: Houston
ORD: Chicago
NRT: Tokyo
JFK: New York
IAD: Washington
DAL: Dallas
YVR: Vancouver
LHR: London

Buckets:
0: LAX: Los Angeles
1: (empty)
2: (empty)
3: SFO: San Francisco
4: IAH: Houston
5: ORD: Chicago --> NRT: Tokyo
6: JFK: New York
7: IAD: Washington
8: DAL: Dallas --> YVR: Vancouver
9: LHR: London
10: (empty)

Removing "LAX"

Removing "ORD"

Buckets after removals:
0: (empty)
1: (empty)
2: (empty)
3: SFO: San Francisco
4: IAH: Houston
5: NRT: Tokyo
6: JFK: New York
7: IAD: Washington
8: DAL: Dallas --> YVR: Vancouver
9: LHR: London
10: (empty)
```

## Concepts Demonstrated

- Hash tables
- Separate chaining collision resolution
- Linked lists
- Object-oriented design
- Abstract base classes (ABCs)
- Type annotations and modern Python development practices

## Improvements over the Textbook Implementation

- Refactored common functionality into shared generic `MapADT` and `HashTable` abstractions.
- Added complete type annotations throughout the project.
- Added module, class, and method docstrings.
- Cached the number of stored entries for constant-time length retrieval.
- Used `zip()` instead of parallel index-based iteration in the demonstration program.
- Improved readability through descriptive naming and PEP 8 formatting.
- Organized the project using snake_case module names.

## Acknowledgements

This project is based on the hash table with separate chaining implementation presented in:

> Lysecky, R., & Vahid, F. (2018, June). *Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithm.
