from __future__ import annotations

from dataclasses import dataclass
from huffman_tree_node import HuffmanTreeNode


@dataclass
class HuffmanCompressedString:
    """Stores a Huffman-compressed string and its decoding tree.

        Attributes:
            uncompressed: The original uncompressed string.
            compressed: The binary Huffman encoding represented as a string of
                0s and 1s.
            root: The root node of the Huffman tree used for decompression.
    """

    uncompressed: str
    compressed: str
    root: HuffmanTreeNode
