from __future__ import annotations

import heapq
from collections import Counter

from huffman_compressed_string import HuffmanCompressedString
from huffman_tree_node import HuffmanTreeNode


class Huffman:
    """Provides methods for Huffman encoding and decoding."""

    @staticmethod
    def _build_frequency_table(input_string: str) -> dict[str, int]:
        """Build a frequency table for characters in a string.

        Args:
            input_string: The string to analyze.

        Returns:
            A dictionary mapping characters to their occurrence counts.
        """
        return dict(Counter(input_string))

    @staticmethod
    def build_tree(input_string: str) -> HuffmanTreeNode:
        """Build a Huffman tree from an input string.

        Args:
            input_string: The string to build the tree from.

        Returns:
            The root node of the Huffman tree.
        """
        frequency_table = Huffman._build_frequency_table(input_string)

        # Make a priority queue of nodes
        nodes: list[HuffmanTreeNode] = [
            HuffmanTreeNode.create_leaf(character, frequency)
            for character, frequency in frequency_table.items()
        ]

        heapq.heapify(nodes)

        # Make parent nodes up to the root
        while len(nodes) > 1:
            # Dequeue two lowest priority nodes
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)

            # Enqueue parent back into priority queue
            heapq.heappush(nodes, HuffmanTreeNode(left, right))

        return nodes[0]

    @staticmethod
    def _build_codes(
        node: HuffmanTreeNode, prefix: str, output: dict[str, str]
    ) -> None:
        """Generate Huffman codes for each character.

        Args:
            node: Current node in the Huffman tree.
            prefix: Current binary prefix.
            output: Dictionary storing character-to-code mappings.
        """
        if node.is_leaf():
            assert node.character is not None
            output[node.character] = prefix or "0"
            return

        assert node.left_child is not None
        assert node.right_child is not None

        Huffman._build_codes(node.left_child, prefix + "0", output)
        Huffman._build_codes(node.right_child, prefix + "1", output)

    @staticmethod
    def compress(input_string: str) -> HuffmanCompressedString | None:
        """Compress a string using Huffman encoding.

        Args:
            input_string: The string to compress.

        Returns:
            A HuffmanCompressedString containing the encoded data and tree,
            or None if the input is empty.
        """
        if not input_string:
            return None

        # Build the Huffman tree
        root = Huffman.build_tree(input_string)

        # Get the compression codes from the tree
        codes: dict[str, str] = {}
        Huffman._build_codes(root, "", codes)

        # Build the compressed result
        compressed = "".join(codes[character] for character in input_string)

        return HuffmanCompressedString(input_string, compressed, root)

    @staticmethod
    def decompress(compressed_string: str, tree_root: HuffmanTreeNode) -> str:
        """Decode a Huffman-compressed string.

        Args:
            compressed_string: The encoded binary string.
            tree_root: Root of the Huffman tree.

        Returns:
            The original uncompressed string.
        """

        if tree_root.is_leaf():
            assert tree_root.character is not None
            return tree_root.character * len(compressed_string)

        node = tree_root
        result: list[str] = []

        for bit in compressed_string:
            # Go left or right based on bit_char value
            if bit == "0":
                assert node.left_child is not None
                node = node.left_child
            else:
                assert node.right_child is not None
                node = node.right_child

            # If the node is a leaf, add the character to the decompressed
            # result and go back to the root node
            if node.is_leaf():
                assert node.character is not None
                result.append(node.character)
                node = tree_root

        return "".join(result)
