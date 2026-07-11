from dataclasses import dataclass
from huffman_tree_node import HuffmanTreeNode


@dataclass
class HuffmanCompressedString:
    uncompressed: str
    compressed: str
    root: HuffmanTreeNode