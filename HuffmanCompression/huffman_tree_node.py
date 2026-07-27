from __future__ import annotations

from dataclasses import dataclass


@dataclass
class HuffmanTreeNode:
    """Represents a node in a Huffman encoding tree.

    Leaf nodes contain a character and its frequency.
    Internal nodes contain references to child nodes and store the combined
    frequency of their children.
    """

    left_child: HuffmanTreeNode | None
    right_child: HuffmanTreeNode | None
    character: str | None = None
    frequency: int = 0

    def __post_init__(self) -> None:
        """Calculate the frequency for an internal node.

        Leaf nodes provide their own frequency when created through
        `create_leaf()`. Internal nodes calculate their frequency by summing
        the frequencies of their children.
        """
        if self.character is None:
            if self.left_child is not None:
                self.frequency += self.left_child.frequency
            if self.right_child is not None:
                self.frequency += self.right_child.frequency

    @classmethod
    def create_leaf(cls, leaf_character: str, leaf_frequency: int) -> HuffmanTreeNode:
        """Create a leaf node containing a character and frequency.

        Args:
            leaf_character: The character stored in the leaf.
            leaf_frequency: The number of occurrences of the character.

        Returns:
            A HuffmanTreeNode representing a leaf.
        """
        return cls(None, None, character=leaf_character, frequency=leaf_frequency)

    def is_leaf(self) -> bool:
        """Determine whether this node is a leaf node.

        Returns:
            True if this node has no children; otherwise, False.
        """
        return self.left_child is None and self.right_child is None

    def __lt__(self, other: HuffmanTreeNode) -> bool:
        """Compare nodes by frequency for priority queue ordering."""
        return self.frequency < other.frequency
