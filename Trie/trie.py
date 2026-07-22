from __future__ import annotations

from Trie.trie_node import TrieNode

_TERMINAL_MARKER = "\0"
type SearchResult = tuple[TrieNode | None, int]


class Trie:
    """A trie (prefix tree) for efficient string storage and lookup.

    A trie stores strings character-by-character, allowing efficient prefix-based
    search operations.
    """
    def __init__(self) -> None:
        """Initialize an empty trie."""
        self.root: TrieNode = TrieNode()

    def contains(self, text_string: str) -> bool:
        """Check if the trie contains a given string.

        Args:
            text_string: The string to check for.
        """
        search_result = self.search(text_string)
        return search_result[0] is not None

    def contains_with_count(self, text_string: str) -> tuple[bool, int]:
        """Check if the trie contains a given string and return the number of nodes visited.

        Args:
            text_string: The string to check for.

        Returns:
            A tuple containing a boolean indicating if the string is in the trie and an integer representing the number of nodes visited.
        """
        search_result = self.search(text_string)
        return search_result[0] is not None, search_result[1]

    def insert(self, text_string: str) -> None:
        """Insert a new string into the trie.

        Args:
            text_string: The string to insert.

        Returns:
            None.
        """
        node = self.root

        # Iterate through each character in text_string
        for character in text_string:
            child = node.get_child(character)
            if child is None:
                # Add a new child
                child = node.add_child(character)
            node = child
        if node.get_child(_TERMINAL_MARKER) is None:
            node.add_child(_TERMINAL_MARKER)

    def remove(self, text_string: str) -> bool:
        """Remove a string from the trie via a call to the recursive helper function.

        Args:
            text_string: The string to remove.

        Returns:
            True if the string was removed; otherwise, False.
        """
        return self._remove_recursive(self.root, text_string, 0)

    def _remove_recursive(
            self,
            node: TrieNode,
            text_string: str,
            char_index: int
    ) -> bool:
        """Recursively remove a string from the trie.

        Args:
            node: The current node being examined.
            text_string: The string to remove.
            char_index: The current character index being examined.

        Returns:
            True if the string existed and was removed; otherwise, False.
        """
        if char_index == len(text_string):
            if node.get_child(_TERMINAL_MARKER) is not None:
                node.remove_child(_TERMINAL_MARKER)
                return True
            return False # text_string not found

        character = text_string[char_index]
        child = node.get_child(character)
        if child is None:
            return False
        removed = self._remove_recursive(child, text_string, char_index + 1)
        if removed and child.get_child_count() == 0:
            node.remove_child(character)
        return removed

    def search(self, text_string: str) -> SearchResult:
        """Search for a string in the trie.

        Args:
            text_string: The string to search for.

        Returns:
            A tuple containing the terminal marker node if the string exists,
            otherwise None, and the number of nodes visited.
        """
        node = self.root

        nodes_visited = 0
        for character in text_string:
            child = node.get_child(character)
            if child is None:
                return None, nodes_visited
            nodes_visited += 1
            node = child
        nodes_visited += 1
        return node.get_child(_TERMINAL_MARKER), nodes_visited
