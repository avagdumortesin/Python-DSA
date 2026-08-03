# Hash Table with Double Hashing

## Overview

This project demonstrates a Python implementation of a **hash table using double hashing** to resolve collisions. The implementation is based on the example presented in the WGU zyBooks *Data Structures and Algorithms II* textbook but has been refactored using modern Python features while preserving the original algorithm.

Double hashing is an open-addressing collision-resolution strategy. When a collision occurs, the algorithm computes a second hash value to determine the probe interval, producing a probe sequence that is unique for each key. Compared to linear and quadratic probing, double hashing reduces clustering by spreading collisions more uniformly throughout the table.

This implementation distinguishes between buckets that have never contained an item and buckets that became empty after removal. This allows searches to continue through deleted positions without incorrectly terminating a probe sequence.

This implementation shares common map and hash table abstractions with the other collision-resolution strategies in this repository, allowing each implementation to focus on its collision-resolution strategy.

## Features

- Hash table implementation using double hashing
- Open-addressing collision resolution
- Secondary hash function for probe-step calculation
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
├── Double_Hashing/
│   ├── double_hashing_hash_table.py
│   ├── main.py
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
0: YVR: Vancouver
1: IAH: Houston
2: IAD: Washington
3: SFO: San Francisco
4: ORD: Chicago
5: NRT: Tokyo
6: JFK: New York
7: LHR: London
8: DAL: Dallas
9: EMPTY_SINCE_START
10: LAX: Los Angeles

Removing "LAX"

Removing "ORD"

Buckets after removals:
0: YVR: Vancouver
1: IAH: Houston
2: IAD: Washington
3: SFO: San Francisco
4: EMPTY_AFTER_REMOVAL
5: NRT: Tokyo
6: JFK: New York
7: LHR: London
8: DAL: Dallas
9: EMPTY_SINCE_START
10: EMPTY_AFTER_REMOVAL
```

## Concepts Demonstrated

- Hash tables
- Open addressing
- Double hashing
- Collision resolution
- Secondary hash functions
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
- Centralized the double-hashing probe calculation in `bucket_index()`.
- Encapsulated the secondary hash function in a dedicated helper method.
- Added validation for table capacity.
- Preserved deleted buckets using an `EMPTY_AFTER_REMOVAL` sentinel.
- Prevented duplicate keys by continuing past removed buckets during insertion.
- Cached the number of stored entries for constant-time length retrieval.
- Added complete type annotations throughout the project.
- Added module, class, and method docstrings.
- Used `zip()` instead of parallel index-based iteration in the demonstration program.
- Improved readability through descriptive naming and PEP 8 formatting.
- Organized the project using snake_case module names.

## Acknowledgements

This project is based on the double hashing hash table implementation presented in:

> Lysecky, R., & Vahid, F. (2018, June). *Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithm.