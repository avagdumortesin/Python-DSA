from __future__ import annotations


class TrieNode:
    """Represents a single node in a trie."""

    def __init__(self):
        self.children: dict[str, TrieNode] = {}

    def add_child(self, character: str) -> TrieNode:
        """Create a new child node for the given character.

        Args:
            character: the character to add as a child node.

        Returns:
            A new TrieNode object.
        """
        new_node = TrieNode()
        self.children[character] = new_node
        return new_node

    def get_child(self, character: str) -> TrieNode | None:
        """Return the child node corresponding to `character`.

        Args:
            character: the character to get the child node for.

        Returns:
            The child node if it exists, otherwise None.
        """
        return self.children.get(character)

    def get_child_count(self) -> int:
        """Return the number of child nodes.

        Returns:
            The number of child nodes.
        """
        return len(self.children)

    def remove_child(self, character: str) -> bool:
        """Remove the child node for the given character.

        Args:
            character: the character to remove the child node for.

        Returns:
            True if the child node was removed, otherwise False.
        """
        if character in self.children:
            del self.children[character]
            return True
        return False
