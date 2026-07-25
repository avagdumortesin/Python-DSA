from __future__ import annotations
from enum import Enum, auto


class NodeColor(Enum):
    """Colors available to a red-black tree node."""

    RED = auto()
    BLACK = auto()


class RBTNode:
    """Represent a node in a red-black tree."""

    def __init__(
        self,
        node_key: int,
        parent_node: RBTNode | None = None,
        color: NodeColor = NodeColor.RED,
        left_child: RBTNode | None = None,
        right_child: RBTNode | None = None,
    ) -> None:
        """Initialize a red-black tree node.

        Args:
            node_key: The key value stored in the node.
            parent_node: The node's parent.
            color: The color of the node.
            left_child: The node's left child.
            right_child: The node's right child.
        """
        self.key = node_key
        self.parent = parent_node
        self.left = left_child
        self.right = right_child
        self.color = color

    def are_both_children_black(self) -> bool:
        """Check if both children of this node are black.

        A missing child is considered black.

        Returns:
            True if neither child is red; otherwise, False.
        """
        return ((self.left is None or self.left.is_black()) and
                (self.right is None or self.right.is_black()))

    def count(self) -> int:
        """Count the number of nodes in the subtree rooted at this node.

        Returns:
            The number of nodes in the subtree.
        """
        count = 1
        if self.left is not None:
            count += self.left.count()
        if self.right is not None:
            count += self.right.count()
        return count

    def get_grandparent(self) -> RBTNode | None:
        """Return the grandparent of this node.

        Returns:
            The grandparent node, or None if it does not exist.
        """
        if self.parent is None:
            return None

        return self.parent.parent

    def get_predecessor(self) -> RBTNode:
        """Return the predecessor from this node's left subtree.

        Returns:
            The rightmost node in the left subtree.

        Raises:
            AssertionError: If the node has no left child.
        """
        node = self.left
        assert node is not None

        while node.right is not None:
            node = node.right

        return node

    def get_sibling(self) -> RBTNode | None:
        """Return the sibling of this node.

        Returns:
            The sibling node, or None if it does not exist.
        """
        parent = self.parent
        if parent is None:
            return None

        if self is parent.left:
            return parent.right

        return parent.left

    def get_uncle(self) -> RBTNode | None:
        """Return the uncle of this node.

        Returns:
            The uncle node, or None if it does not exist.
        """
        grandparent = self.get_grandparent()

        if grandparent is None:
            return None

        if self.parent is grandparent.left:
            return grandparent.right

        return grandparent.left

    def is_black(self) -> bool:
        """Determine whether this node is black.

        Returns:
            True if the node is black; otherwise, False.
        """
        return self.color is NodeColor.BLACK

    def is_red(self) -> bool:
        """Determine whether this node is red.

        Returns:
            True if the node is red; otherwise, False.
        """
        return self.color is NodeColor.RED

    def replace_child(
        self,
        current_child: RBTNode,
        new_child: RBTNode | None,
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

    def set_left(self, new_left: RBTNode | None) -> None:
        """Set the left child and update related node information.

        Args:
            new_left: The node to assign as the left child, or None to remove
                the current left child.
        """

        self.left = new_left

        if new_left is not None:
            new_left.parent = self

    def set_right(self, new_right: RBTNode | None) -> None:
        """Set the right child and update related node information.

        Args:
            new_right: The node to assign as the right child, or None to remove
                the current right child.
        """
        self.right = new_right

        if new_right is not None:
            new_right.parent = self
