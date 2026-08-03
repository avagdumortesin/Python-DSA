# Hash Table with Quadratic Probing

## Overview

This project demonstrates a Python implementation of a **hash table using quadratic probing** to resolve collisions. The implementation is based on the example presented in the WGU zyBooks *Data Structures and Algorithms II* textbook but has been refactored using modern Python features while preserving the original algorithm.

Quadratic probing is an open-addressing collision-resolution strategy. When a collision occurs, the algorithm checks additional buckets using a quadratic probe sequence rather than examining consecutive buckets. This helps reduce the primary clustering associated with linear probing.

The implementation distinguishes between buckets that have never contained an item and buckets that became empty after removal. This allows searches to continue through deleted positions without incorrectly terminating a probe sequence.

## Features

- Hash table implementation using quadratic probing
- Open-addressing collision resolution
- Configurable linear and quadratic probing coefficients
- Generic key and value types
- Special bucket states for unused and removed entries
- Dictionary-style lookup through subscription syntax
- Constant-time retrieval of the number of stored items
- Fully type-annotated implementation
- Comprehensive module, class, and method docstrings
- Demonstration of insertion, removal, and bucket visualization

## Project Structure

```text
.
├── hash_table.py
├── main.py
├── map_adt.py
├── open_addressing_bucket.py
├── quadratic_probing_hash_table.py
└── README.md
```

## Running the Example

Run the demonstration from the project directory:

```bash
python main.py
```

Example output (bucket assignments will vary because Python randomizes string hashes between interpreter sessions):

```text
Buckets:
0: DAL: Dallas
1: ORD: Chicago
2: IAH: Houston
3: SFO: San Francisco
4: IAD: Washington
5: EMPTY_SINCE_START
6: NRT: Tokyo
7: EMPTY_SINCE_START
8: JFK: New York
9: EMPTY_SINCE_START
10: EMPTY_SINCE_START
11: EMPTY_SINCE_START
12: LAX: Los Angeles

Removing "LAX"

Removing "ORD"

Buckets after removals:
0: DAL: Dallas
1: EMPTY_AFTER_REMOVAL
2: IAH: Houston
3: SFO: San Francisco
4: IAD: Washington
5: EMPTY_SINCE_START
6: NRT: Tokyo
7: EMPTY_SINCE_START
8: JFK: New York
9: EMPTY_SINCE_START
10: EMPTY_SINCE_START
11: EMPTY_SINCE_START
12: EMPTY_AFTER_REMOVAL
```

## Concepts Demonstrated

- Hash tables
- Open addressing
- Quadratic probing
- Collision resolution
- Probe sequences
- Tombstone-based deletion
- Generic programming with type variables
- Abstract Base Classes
- Object-oriented design
- Type annotations and modern Python development practices

## Improvements over the Textbook Implementation

- Replaced informal base classes with formal Abstract Base Classes.
- Introduced generic key and value types using `TypeVar`.
- Implemented dictionary-style lookup through `__getitem__()`.
- Added a shared `get()` implementation that supports default values.
- Added explicit bucket-state methods for unused and removed entries.
- Centralized the quadratic probing calculation in `bucket_index()`.
- Added configurable `c1` and `c2` probing coefficients.
- Added validation for table capacity and probing coefficients.
- Preserved deleted buckets using an `EMPTY_AFTER_REMOVAL` sentinel.
- Prevented duplicate keys by continuing past removed buckets during insertion.
- Cached the number of stored entries for constant-time length retrieval.
- Added complete type annotations throughout the project.
- Added module, class, and method docstrings.
- Used `zip()` instead of parallel index-based iteration in the demonstration program.
- Improved readability through descriptive naming and PEP 8 formatting.
- Organized the project using snake_case module names.

## Acknowledgements

This project is based on the quadratic probing hash table implementation presented in:

> Lysecky, R., & Vahid, F. (2018, June). *Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithm.
