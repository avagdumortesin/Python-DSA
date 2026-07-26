# Huffman Compression

## Overview

This repository contains a modern Python implementation of the **Huffman compression** algorithm. While the underlying algorithm follows the implementation presented in the ZyBooks *Data Structures and Algorithms II* textbook, the codebase has been refactored to emphasize readability, maintainability, static type safety, and modern Python best practices.

Huffman coding is a lossless compression algorithm that assigns shorter binary codes to more frequently occurring characters, reducing the total number of bits required to represent a string.

## Features

-   Build Huffman trees from character frequencies
-   Compress strings using Huffman encoding
-   Decompress encoded strings back to their original form
-   Automatic frequency analysis using `collections.Counter`
-   Efficient priority queue implementation using `heapq`
-   Dataclass-based models
-   Comprehensive type hints
-   PEP 8 compliant formatting
-   Comprehensive docstrings throughout

## Project Structure

``` text
.
├── huffman.py
├── huffman_tree_node.py
├── huffman_compressed_string.py
└── README.md
```

## Running the Example

Run the demonstration from the project directory:

``` bash
python main.py
```

Example output:

``` text
Huffman compression demonstration:
Original message:   the quick brown fox jumps over the lazy dog
Compressed data:    100011011101000111010100110111110110011001100111110111100101100001101000010111001010110100011111001011101100101111110001011101110101111000100011011101000011010110011100111100000110001010110101
Restored message:   the quick brown fox jumps over the lazy dog

Original size:      344 bits
Compressed size:    192 bits
Space reduction:    44.19%
Successful restore: True
```

## Concepts Demonstrated

-   Huffman coding
-   Binary trees
-   Priority queues (heaps)
-   Frequency analysis
-   Recursive tree traversal
-   Lossless data compression
-   Dataclasses
-   Static type annotations
-   Object-oriented programming

## Improvements over the Textbook Implementation

-   Modern Python type annotations throughout
-   Dataclass implementations for tree nodes and compressed data containers
-   Replacement of `queue.PriorityQueue` with the lighter-weight `heapq` module
-   Use of `collections.Counter` for concise frequency table construction
-   Removal of Java-style getter methods in favor of direct attribute access
-   Private helper methods for internal implementation details
-   An `is_leaf()` helper to simplify traversal logic
-   Comprehensive docstrings for modules, classes, and methods
-   More descriptive variable and method names
-   Handling of the single-character edge case during compression and decompression
-   Cleaner string construction using `str.join()`
-   Assertions to document internal invariants

## Acknowledgements

This project is based on the Huffman coding algorithms presented in:

> Lysecky, R., & Vahid, F. (2018, June). *C950: Data Structures and Algorithms II*. zyBooks.

The implementation has been refactored and modernized for readability, maintainability, and current Python best practices while preserving the original algorithms.
