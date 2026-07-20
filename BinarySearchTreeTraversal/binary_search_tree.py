from __future__ import annotations
from BinarySearchTreeTraversal.bst_node import BSTNode
from BinarySearchTreeTraversal.bst_node_visitor import BSTNodeVisitor

class BinarySearchTree:
    """A binary search tree implementation.

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

    def get_root(self) -> BSTNode | None:
        """Return the root node of the tree."""
        return self.root

    def in_order_traversal(self, visitor: BSTNodeVisitor) -> None:
        """Perform an in-order traversal of the tree.

        Args:
            visitor: A visitor object implementing the `BSTNodeVisitor` interface.

        Returns:
            None.
        """
        self._in_order_traversal(self.root, visitor)

    def _in_order_traversal(
            self,
            node: BSTNode | None,
            visitor: BSTNodeVisitor
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
            # Duplicate keys are not allowed
            return False
        # Create and insert a new node and return True
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
            new_node.parent = None
            return
        current_node = self.root
        while current_node is not None:
            if new_node.key < current_node.key:
                # If no left child exists, add the new node here, otherwise
                # repeat from the left child.
                if current_node.left is None:
                    current_node.left = new_node
                    new_node.parent = current_node
                    return
                else:
                    current_node = current_node.left
            else:
                # If no right child exists, add the new node here, otherwise
                # repeat from the right child.
                if current_node.right is None:
                    current_node.right = new_node
                    new_node.parent = current_node
                    return
                else:
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
            self.remove_node(node)
            return True
        return False

    def remove_node(self, node: BSTNode) -> None:
        """Remove the specified node from the tree.

        Args:
            node: The BSTNode to remove.

        Returns:
            None.
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
            self.remove_node(successor)

        # Case 2: Root node (with 1 or 0 children)
        elif node is self.root:
            if node.left is not None:
                self.root = node.left
            else:
                self.root = node.right
            # The new root, if not None, must have parent assigned with None
            if self.root is not None:
                self.root.parent = None

        # Case 3: Internal with left child only
        elif node.left is not None:
            node.parent.replace_child(node, node.left)

        # Case 4: Internal node with only a right child, or a leaf node
        else:
            node.parent.replace_child(node, node.right)

    def search(self, search_key: int) -> BSTNode | None:
        """Search the tree for a node with the specified key.

        Args:
            search_key: The key value to locate.

        Returns:
            The BSTNode containing the key if found; otherwise, None.
        """
        current_node = self.root
        while current_node is not None:
            if current_node.key == search_key:
                return current_node
            elif search_key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None
