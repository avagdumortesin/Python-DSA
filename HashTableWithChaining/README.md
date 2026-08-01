# Hash Table with Separate Chaining

## Overview

This project demonstrates a Python implementation of a **hash table using separate chaining** to resolve collisions. The implementation is based on the example presented in the WGU zyBooks *Data Structures and Algorithms II* textbook but has been refactored using modern Python features while preserving the original algorithm.

Separate chaining stores colliding entries in linked lists associated with each bucket of the hash table. This implementation supports insertion, lookup, removal, containment checks, and formatted display of both the table contents and the underlying bucket structure.

## Features

- Hash table implementation using separate chaining
- Generic key and value types
- Collision resolution using linked lists
- Separate abstract `MapADT` and `HashTable` base classes
- Dataclass-based linked-list nodes
- Fully type-annotated implementation
- Comprehensive documentation through module, class, and method docstrings
- Demonstration of insertion, removal, and bucket visualization

## Project Structure

```text
.
├── chaining_hash_table.py
├── hash_table.py
├── main.py
├── map_adt.py
└── README.md
```

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
- Generic programming with type variables
- Abstract Base Classes (ABC)
- Object-oriented design
- Python dataclasses
- Type annotations and modern Python development practices

## Improvements over the Textbook Implementation

- Replaced manual node classes with `@dataclass(slots=True)`.
- Introduced generic key and value types using `TypeVar`.
- Replaced the informal map interface with an Abstract Base Class.
- Implemented dictionary-style lookup through `__getitem__()` while preserving a `get()` convenience method.
- Added complete type annotations throughout the project.
- Added module, class, and method docstrings.
- Introduced a reusable `bucket_index()` helper to centralize bucket computation.
- Cached the number of stored entries for constant-time length retrieval.
- Used `zip()` instead of parallel index-based iteration in the demonstration program.
- Improved readability through descriptive naming and PEP 8 formatting.
- Organized the project using snake_case module names.

## Acknowledgements

This project is based on the hash table with separate chaining implementation presented in:

> Lysecky, R., & Vahid, F. (2018, June). *Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithm.



