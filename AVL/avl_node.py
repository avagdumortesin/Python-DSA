from __future__ import annotations


class AVLNode:
    """A node in an AVL tree."""

    def __init__(self, node_key: int) -> None:
        """Initialize an AVL tree node.

        Args:
            node_key: The key value stored in the node.
        """
        self.key: int = node_key
        self.parent: AVLNode | None = None
        self.left: AVLNode | None = None
        self.right: AVLNode | None = None
        self.height: int = 0

    def get_balance(self) -> int:
        """Return the balance factor of this node.

        Returns:
            The height of the left subtree minus the height of the right
            subtree.
        """
        left_height = self.left.height if self.left is not None else -1
        right_height = self.right.height if self.right is not None else -1

        return left_height - right_height

    def replace_child(
        self,
        current_child: AVLNode,
        new_child: AVLNode | None,
    ) -> bool:
        """Replace one of this node's children.

        Args:
            current_child: The existing child to replace.
            new_child: The node that will replace the existing child, or None
                to remove the child without replacing it.

        Returns:
            True if the existing child was found and replaced; otherwise,
            False.
        """
        if self.left is current_child:
            self.set_left(new_child)
            return True

        if self.right is current_child:
            self.set_right(new_child)
            return True

        return False

    def set_left(self, new_left: AVLNode | None) -> None:
        """Set the left child and update related node information.

        Args:
            new_left: The node to assign as the left child, or None to remove
                the current left child.
        """
        self.left = new_left

        if self.left is not None:
            self.left.parent = self

        self.update_height()

    def set_right(self, new_right: AVLNode | None) -> None:
        """Set the right child and update related node information.

        Args:
            new_right: The node to assign as the right child, or None to remove
                the current right child.
        """
        self.right = new_right

        if self.right is not None:
            self.right.parent = self

        self.update_height()

    def update_height(self) -> None:
        """Recalculate the height of the subtree rooted at this node."""
        left_height = self.left.height if self.left is not None else -1
        right_height = self.right.height if self.right is not None else -1

        self.height = max(left_height, right_height) + 1
