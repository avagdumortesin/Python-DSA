# Hash Table with Linear Probing

## Overview

This project demonstrates a Python implementation of a **hash table using linear probing** to resolve collisions. The implementation is based on the example presented in the WGU zyBooks *Data Structures and Algorithms II* textbook but has been refactored using modern Python features while preserving the original algorithm.

Linear probing is an open-addressing collision-resolution strategy. When a collision occurs, the algorithm checks the next consecutive bucket in the hash table until an empty slot is found or the entire table is traversed. This implementation distinguishes between buckets that have never contained an item and buckets that became empty after removal. This allows searches to continue through deleted positions without incorrectly terminating a probe sequence.

This implementation shares common map and hash table abstractions with the other collision-resolution strategies in this repository, allowing each implementation to focus on its collision-resolution strategy.

## Features

- Hash table implementation using linear probing
- Open-addressing collision resolution
- Shared `MapADT` and `HashTable` framework with algorithm-specific collision handling
- Special bucket states for unused and removed entries
- Dictionary-style lookup through subscription syntax
- Constant-time retrieval of the number of stored items
- Fully type-annotated implementation
- Comprehensive documentation through module, class, and method docstrings
- Demonstration of insertion, removal, and bucket visualization

## Project Structure

```text
HashTableAlgorithms/
├── Linear_Probing/
│   ├── main.py
│   ├── linear_probing_hash_table.py
│   └── README.md
└── shared/
    ├── __init__.py
    ├── hash_table.py
    ├── map_adt.py
    ├── open_addressing_bucket.py
    └── README.md
```

## Shared Components

This implementation uses the common map and hash-table abstractions located in
`HashTableAlgorithms/shared`.

- `map_adt.py` defines the generic map interface.
- `hash_table.py` provides shared hash-table behavior.
- `open_addressing_bucket.py` provides bucket states for open addressing.

See the [`shared` README](../shared/README.md) for additional details.

## Running the Example

Run the demonstration from the project directory:

```bash
python main.py
```

Example output (bucket assignments will vary because Python randomizes string hashes between interpreter sessions):

```text
Buckets:
0: EMPTY_SINCE_START
1: ORD: Chicago
2: LAX: Los Angeles
3: IAH: Houston
4: DAL: Dallas
5: JFK: New York
6: SFO: San Francisco
7: IAD: Washington
8: LHR: London
9: NRT: Tokyo
10: YVR: Vancouver

Removing "LAX"

Removing "ORD"

Buckets after removals:
0: EMPTY_SINCE_START
1: EMPTY_AFTER_REMOVAL
2: EMPTY_AFTER_REMOVAL
3: IAH: Houston
4: DAL: Dallas
5: JFK: New York
6: SFO: San Francisco
7: IAD: Washington
8: LHR: London
9: NRT: Tokyo
10: YVR: Vancouver
```

## Concepts Demonstrated

- Hash tables
- Open addressing
- Linear probing
- Collision resolution
- Probe sequences
- Tombstone-based deletion
- Shared reusable abstractions
- Generic programming with type variables
- Abstract Base Classes (ABCs)
- Object-oriented design
- Type annotations and modern Python development practices

## Improvements over the Textbook Implementation

- Refactored common hash-table functionality into shared infrastructure.
- Added explicit bucket-state methods for unused and removed entries.
- Centralized the linear probing formula in `bucket_index()`.
- Preserved deleted buckets using an `EMPTY_AFTER_REMOVAL` sentinel.
- Prevented duplicate keys by continuing past removed buckets during insertion.
- Cached the number of stored entries for constant-time length retrieval.
- Added complete type annotations throughout the project.
- Added module, class, and method docstrings.
- Used `zip()` instead of parallel index-based iteration in the demonstration program.
- Improved readability through descriptive naming and PEP 8 formatting.
- Organized the project using snake_case module names.

## Acknowledgements

This project is based on the linear probing hash table implementation presented in:

> Lysecky, R., & Vahid, F. (2018, June). *Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithm.
