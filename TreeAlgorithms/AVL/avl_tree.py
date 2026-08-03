from TreeAlgorithms.AVL.avl_node import AVLNode
from TreeAlgorithms.AVL.avl_print import AVLPrint


class AVLTree:
    """A self-balancing binary search tree."""

    def __init__(self) -> None:
        """Initialize an empty AVL tree."""
        self.root: AVLNode | None = None

    def contains(self, key: int) -> bool:
        """Determine whether a key exists in the tree.

        Args:
            key: The key value to search for.

        Returns:
            True if the key exists in the tree; otherwise, False.
        """
        return self.search(key) is not None

    def insert_key(self, key: int) -> bool:
        """Insert a key if it does not already exist.

        Args:
            key: The key to insert.

        Returns:
            True if the key was inserted; otherwise, False.
        """
        if self.contains(key):
            return False

        self._insert_node(AVLNode(key))
        return True

    def _insert_node(self, node: AVLNode) -> None:
        """Insert a node and _rebalance its ancestors.

        Args:
            node: The node to insert.
        """
        if self.root is None:
            self.root = node
            return

        current_node = self.root

        while True:
            if node.key < current_node.key:
                if current_node.left is None:
                    current_node.set_left(node)
                    break

                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.set_right(node)
                    break

                current_node = current_node.right

        current_node = node.parent
        while current_node is not None:
            self._rebalance(current_node)
            current_node = current_node.parent

    def print_tree(self, end: str = "") -> None:
        """Print the tree in a structured format."""
        print(AVLPrint.tree_to_string(self.root), end=end)

    def _rebalance(self, node: AVLNode) -> None:
        """Update a node's height and rebalance its subtree if necessary.

        Args:
            node: The root of the subtree to rebalance.
        """
        node.update_height()

        balance = node.get_balance()

        if balance == -2:
            right_child = node.right
            assert right_child is not None

            if right_child.get_balance() == 1:
                self._rotate_right(right_child)

            self._rotate_left(node)

        elif balance == 2:
            left_child = node.left
            assert left_child is not None

            if left_child.get_balance() == -1:
                self._rotate_left(left_child)

            self._rotate_right(node)

    def remove_key(self, key: int) -> bool:
        """Remove the node containing a specified key.

        Args:
            key: The key to remove.

        Returns:
            True if the key was found and removed; otherwise, False.
        """
        node = self.search(key)
        if node is None:
            return False
        return self._remove_node(node)

    def _remove_node(self, node: AVLNode) -> bool:
        """Remove the specified node from the tree.

        Args:
            node: The AVLNode to remove.

        Returns:
            True after the node is removed.
        """
        parent = node.parent

        # Case 1: Internal node with 2 children
        if node.left is not None and node.right is not None:
            # Find the in-order successor (leftmost node in the right subtree)
            successor = node.right

            while successor.left is not None:
                successor = successor.left

            # Replace the node's key with the successor's key
            node.key = successor.key
            # Recursively remove successor
            return self._remove_node(successor)

        # Case 2: Root node (with 1 or 0 children)
        if node is self.root:
            self.root = node.left if node.left is not None else node.right

            # The new root, if not None, must have parent assigned with None
            if self.root is not None:
                self.root.parent = None
            return True

        assert parent is not None

        # Case 3: Internal with left child only
        if node.left is not None:
            parent.replace_child(node, node.left)

        # Case 4: Internal node with only a right child, or a leaf node
        else:
            parent.replace_child(node, node.right)

        node_to_rebalance: AVLNode | None = parent

        while node_to_rebalance is not None:
            self._rebalance(node_to_rebalance)
            node_to_rebalance = node_to_rebalance.parent

        return True

    def _rotate_left(self, node: AVLNode) -> None:
        """Perform a left rotation on the subtree rooted at `node`.

        Args:
            node: The root of the subtree to rotate.
        """
        parent = node.parent

        right_child = node.right
        assert right_child is not None

        right_left_child = right_child.left

        node.set_right(right_left_child)
        right_child.set_left(node)

        if parent is not None:
            parent.replace_child(node, right_child)
        else:
            self.root = right_child
            right_child.parent = None

    def _rotate_right(self, node: AVLNode) -> None:
        """Perform a right rotation on the subtree rooted at `node`.

        Args:
            node: The root of the subtree to rotate.
        """
        parent = node.parent

        left_child = node.left
        assert left_child is not None

        left_right_child = left_child.right

        node.set_left(left_right_child)
        left_child.set_right(node)

        if parent is not None:
            parent.replace_child(node, left_child)
        else:
            self.root = left_child
            left_child.parent = None

    def search(self, key: int) -> AVLNode | None:
        """Search the tree for a node with the specified key.

        Args:
            key: The key value to locate.

        Returns:
            The AVLNode that contains the key if found; otherwise, None.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: AVLNode | None, key: int) -> AVLNode | None:
        """Recursively search the subtree rooted at `node` for `key`.

        Args:
            node: The root of the subtree to search.
            key: The key value to locate.

        Returns:
            The matching AVLNode if found; otherwise, None.
        """
        if node is None:
            return None

        if key == node.key:
            return node

        if key < node.key:
            return self._search_recursive(node.left, key)

        return self._search_recursive(node.right, key)
