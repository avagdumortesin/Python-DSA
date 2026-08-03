# Shared Hash Table Components

This directory contains reusable infrastructure shared by the hash table
implementations in this repository. These modules define the common interfaces
and supporting classes that allow each collision-resolution strategy to focus
only on its algorithm-specific behavior.

## Files

### `map_adt.py`

Defines the abstract `MapADT` interface implemented by all hash tables.

Responsibilities include:

- Determining whether a key exists
- Retrieving values
- Inserting and updating key-value pairs
- Removing items
- Reporting the number of stored entries
- Printing map contents

---

### `hash_table.py`

Provides the abstract base class for hash table implementations.

Responsibilities include:

- Computing a non-negative hash value
- Defining the `print_table()` interface
- Serving as the common parent for all hash table algorithms

---

### `open_addressing_bucket.py`

Defines the bucket type used by open-addressing hash tables.

Each bucket stores:

- a key
- a value

It also provides two sentinel bucket objects:

- `EMPTY_SINCE_START`
- `EMPTY_AFTER_REMOVAL`

These sentinel values are used by:

- Linear Probing
- Quadratic Probing
- Double Hashing

Chaining does not use this class because collisions are resolved with linked
lists instead of open addressing.

## Used By

| Algorithm         | Uses                                          |
|-------------------|-----------------------------------------------|
| Chaining          | `MapADT`, `HashTable`                         |
| Linear Probing    | `MapADT`, `HashTable`, `OpenAddressingBucket` |
| Quadratic Probing | `MapADT`, `HashTable`, `OpenAddressingBucket` |
| Double Hashing    | `MapADT`, `HashTable`, `OpenAddressingBucket` |

## Design

Separating these shared components avoids duplicating infrastructure across
multiple implementations while allowing each algorithm to focus on its probing
or collision-resolution strategy.