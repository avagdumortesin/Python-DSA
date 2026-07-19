from __future__ import annotations

class BSTNode:
    """Represents a node in a binary search tree."""
    def __init__(self, node_key, left_child = None, right_child = None):
        self.key = node_key
        self.left = left_child
        self.right = right_child