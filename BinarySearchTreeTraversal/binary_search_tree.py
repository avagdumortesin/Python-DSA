from __future__ import annotations

from BinarySearchTreeTraversal.bst_node import BSTNode
from BinarySearchTreeTraversal.bst_node_visitor import BSTNodeVisitor


class BinarySearchTree:
    """A binary search tree implementation with traversal.

    Supports insertion, searching, and removal of nodes while
    maintaining the binary search tree ordering property.
    """

    def __init__(self) -> None:
        """Initialize an empty binary search tree."""
        self.root: BSTNode | None = None

    def contains(self, key: int) -> bool:
        """Determine whether a key exists in the tree.

        Args:
             key: The key value to search for.

        Returns:
            True if the key exists in the tree; otherwise, False.
        """
        return self.search(key) is not None

    def get_height(self) -> int:
        """Return the height of the tree.

        Returns:
            The number of edges in the longest path from the root to a leaf.
            Returns -1 if the tree is empty.
        """
        return self._get_height(self.root)

    def _get_height(self, node: BSTNode | None) -> int:
        """Compute the height of a subtree.

        Args:
            node: The root node of the subtree.

        Returns:
            The height of the subtree that is rooted at `node`, or -1 if `node` is None.
        """
        if node is None:
            return -1
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        return 1 + max(left_height, right_height)

    def in_order_traversal(self, visitor: BSTNodeVisitor) -> None:
        """Perform an in-order traversal of the tree.

        Args:
            visitor: A visitor object implementing the `BSTNodeVisitor` interface.

        Returns:
            None.
        """
        self._in_order_traversal(self.root, visitor)

    def _in_order_traversal(
        self, node: BSTNode | None, visitor: BSTNodeVisitor
    ) -> None:
        """Recursively perform an in-order traversal starting at `node`.

        Args:
            node: The current node in the traversal.
            visitor: The visitor object whose `visit()` method is invoked for
                each node encountered during the traversal.

        Returns:
            None.
        """
        if node is None:
            return
        self._in_order_traversal(node.left, visitor)
        visitor.visit(node)
        self._in_order_traversal(node.right, visitor)

    def insert_key(self, key: int) -> bool:
        """Insert a new key into the tree if it does not already exist.

        Args:
            key: The key value to insert.

        Returns:
            True if the key was inserted; False if the key already exists.
        """
        if self.contains(key):
            return False

        self.insert_node(BSTNode(key))
        return True

    def insert_node(self, new_node: BSTNode) -> None:
        """Insert a new node into the tree.

        Args:
            new_node: The BSTNode to insert into the tree.

        Returns:
            None.
        """
        # Check if tree is empty
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while True:
            if new_node.key < current_node.key:
                # Insert here if the left child is empty.
                if current_node.left is None:
                    current_node.left = new_node
                    new_node.parent = current_node
                    return
                current_node = current_node.left
            else:
                # Insert here if the right child is empty.
                if current_node.right is None:
                    current_node.right = new_node
                    new_node.parent = current_node
                    return
                current_node = current_node.right

    def remove_key(self, key: int) -> bool:
        """Remove a node with the specified key from the tree.

        Args:
            key: The key of the node to remove.

        Returns:
            True if a node was found and removed; otherwise, False.
        """
        node = self.search(key)
        if node is not None:
            self._remove_node(node)
            return True
        return False

    def _remove_node(self, node: BSTNode) -> None:
        """Remove the specified node from the tree.

        Args:
            node: The BSTNode to remove.
        """
        # Case 1: Internal node with 2 children
        if node.left is not None and node.right is not None:
            # Find the in-order successor (leftmost node in the right subtree)
            successor = node.right

            while successor.left is not None:
                successor = successor.left

            # Replace the node's key with the successor's key
            node.key = successor.key
            # Recursively remove successor
            self._remove_node(successor)
            return

        # Case 2: Root node (with 1 or 0 children)
        if node is self.root:
            self.root = node.left if node.left is not None else node.right

            # The new root, if not None, must have parent assigned with None
            if self.root is not None:
                self.root.parent = None

            return

        # Case 3: Internal node with left child only, right child only, or a leaf node
        assert node.parent is not None
        replacement = node.left if node.left is not None else node.right
        node.parent.replace_child(node, replacement)

    def search(self, key: int) -> BSTNode | None:
        """Search the tree for a node with the specified key.
        Args:
            key: The key value to locate

        Returns:
            The BSTNode containing the key if found; otherwise, None.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: BSTNode | None, key: int) -> BSTNode | None:
        """Recursively search the subtree rooted at `node` for `key`.

        Args:
            node: The root of the subtree to search.
            key: The key value to locate.

        Returns:
            The matching BSTNode if found; otherwise, None.
        """
        if node is None:
            return None

        if key == node.key:
            return node

        if key < node.key:
            return self._search_recursive(node.left, key)

        return self._search_recursive(node.right, key)
