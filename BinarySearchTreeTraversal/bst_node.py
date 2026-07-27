from __future__ import annotations


class BSTNode:
    """Represents a node in a binary search tree."""

    def __init__(
        self,
        node_key: int,
        left_child: BSTNode | None = None,
        right_child: BSTNode | None = None,
        parent_node: BSTNode | None = None,
    ) -> None:
        """Initialize a binary search tree node.

        Args:
            node_key: The key value stored in the node.
            left_child: The node's left child.
            right_child: The node's right child.
            parent_node: The node's parent.
        """
        self.key = node_key
        self.left = left_child
        self.right = right_child
        self.parent = parent_node

    def replace_child(
        self,
        current_child: BSTNode,
        new_child: BSTNode | None,
    ) -> bool:
        """Replace one of the node's children with a new child node.

        Args:
            current_child: The existing child node to be replaced.
            new_child: The replacement child, or None to remove the child.

        Returns:
            True if `current_child` was replaced; otherwise, False.
        """
        if self.left is not current_child and self.right is not current_child:
            return False

        if self.left is current_child:
            self.left = new_child
        else:
            self.right = new_child

        current_child.parent = None

        if new_child is not None:
            new_child.parent = self

        return True
