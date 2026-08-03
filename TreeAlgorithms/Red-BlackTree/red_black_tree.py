from rbt_node import NodeColor, RBTNode
from rbt_print import RBTPrint


class RedBlackTree:
    """A red-black tree implementation."""

    def __init__(self) -> None:
        """Initialize an empty red-black tree."""
        self.root: RBTNode | None = None

    def _bst_remove_node(self, node: RBTNode) -> None:
        """Remove the specified node from the tree.

        Args:
            node: The RBTNode to remove.
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
            self._bst_remove_node(successor)
            return

        # Case 2: Root node (with 1 or 0 children)
        if node is self.root:
            self.root = node.left if node.left is not None else node.right

            # The new root, if not None, must have parent assigned with None
            if self.root is not None:
                self.root.parent = None

            return

        # Case 3: Internal node with left child only, right child only, or a leaf node
        parent = node.parent
        assert parent is not None

        replacement = node.left if node.left is not None else node.right
        parent.replace_child(node, replacement)
        node.parent = None

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

    def _get_height(self, node: RBTNode | None) -> int:
        """Compute the height of a subtree.

        Args:
            node: The root node of the subtree.

        Returns:
            The height of the subtree that is rooted at `node`, or
            -1 if `node` is None.
        """
        if node is None:
            return -1
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        return 1 + max(left_height, right_height)

    def get_length(self) -> int:
        """Return the number of nodes in the tree.

        Returns:
            The number of nodes in the tree.
        """
        if self.root is None:
            return 0
        return self.root.count()

    def insert_key(self, key: int) -> bool:
        """Insert a key if it does not already exist.

        Args:
            key: The key to insert.

        Returns:
            True if the key was inserted; otherwise, False.
        """
        if self.contains(key):
            return False

        self._insert_node(RBTNode(key))
        return True

    def _insert_node(self, node: RBTNode) -> None:
        """Insert a node and restore the red-black tree properties.

        Args:
            node: The node to insert.
        """
        if self.root is None:
            self.root = node
            node.color = NodeColor.BLACK
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

        node.color = NodeColor.RED
        self._insertion_balance(node)

    def _insertion_balance(self, node: RBTNode) -> None:
        """Restore red-black tree properties after insertion.

        Args:
            node: The newly inserted node or an ancestor requiring rebalancing.
        """
        parent = node.parent

        if parent is None:
            node.color = NodeColor.BLACK
            return

        if parent.is_black():
            return

        grandparent = node.get_grandparent()
        assert grandparent is not None

        uncle = node.get_uncle()

        if uncle is not None and uncle.is_red():
            uncle.color = NodeColor.BLACK
            parent.color = NodeColor.BLACK
            grandparent.color = NodeColor.RED
            self._insertion_balance(grandparent)
            return

        if node is parent.right and parent is grandparent.left:
            assert parent is not None
            self._rotate_left(parent)
            node = parent
            parent = node.parent

        elif node is parent.left and parent is grandparent.right:
            assert parent is not None
            self._rotate_right(parent)
            node = parent
            parent = node.parent

        parent.color = NodeColor.BLACK
        grandparent.color = NodeColor.RED

        if node is parent.left:
            self._rotate_right(grandparent)
        else:
            self._rotate_left(grandparent)

    @staticmethod
    def _is_none_or_black(node: RBTNode | None) -> bool:
        """Check if a node is None or is black.

        Args:
            node: The node to check.

        Returns:
            True if the node is None or is black; otherwise, False.
        """
        return node is None or node.is_black()

    def _prepare_for_removal(self, node: RBTNode) -> None:
        """Prepare the tree for the removal of a black node.

        Args:
            node: The black node to be removed.
        """
        if self._try_case1(node):
            return

        parent = node.parent
        assert parent is not None

        sibling = node.get_sibling()
        assert sibling is not None

        if self._try_case2(node, sibling):
            sibling = node.get_sibling()
            assert sibling is not None
        if self._try_case3(node, sibling):
            return
        if self._try_case4(node, sibling):
            return
        if self._try_case5(node, sibling):
            sibling = node.get_sibling()
            assert sibling is not None
        if self._try_case6(node, sibling):
            sibling = node.get_sibling()
            assert sibling is not None

        sibling.color = parent.color
        parent.color = NodeColor.BLACK
        if node is parent.left:
            assert sibling.right is not None
            sibling.right.color = NodeColor.BLACK
            self._rotate_left(parent)
        else:
            assert sibling.left is not None
            sibling.left.color = NodeColor.BLACK
            self._rotate_right(parent)

    @staticmethod
    def _try_case1(node: RBTNode) -> bool:
        """Check if the node is red or has no parent.

        Args:
            node: The node to check.

        Returns:
            True if the node is red or has no parent; otherwise, False.
        """
        return node.is_red() or node.parent is None

    def _try_case2(self, node: RBTNode, sibling: RBTNode) -> bool:
        """Handle a red sibling.

        Args:
            node: The node being prepared for removal.
            sibling: The node's sibling.

        Returns:
            True if the case was applied; otherwise, False.
        """
        if sibling.is_black():
            return False

        parent = node.parent
        assert parent is not None

        parent.color = NodeColor.RED
        sibling.color = NodeColor.BLACK

        if node is parent.left:
            self._rotate_left(parent)
        else:
            self._rotate_right(parent)

        return True

    def _try_case3(self, node: RBTNode, sibling: RBTNode) -> bool:
        """Check if the parent is black and the sibling has both children black.

        Args:
            node: The node whose sibling is to be checked.
            sibling: The sibling to check.

        Returns:
            True if the parent is black and the sibling has both children black;
            otherwise, False.
        """
        parent = node.parent
        assert parent is not None

        if parent.is_black() and sibling.are_both_children_black():
            sibling.color = NodeColor.RED
            self._prepare_for_removal(parent)
            return True
        return False

    @staticmethod
    def _try_case4(node: RBTNode, sibling: RBTNode) -> bool:
        """Handle a red parent with a black sibling and black nephews.

        The parent is recolored black and the sibling is recolored red.

        Args:
            node: The node whose sibling is to be checked.
            sibling: The sibling to check.

        Returns:
            True if the parent is red and the sibling has both children black;
            otherwise, False.
        """
        parent = node.parent
        assert parent is not None

        if parent.is_red() and sibling.are_both_children_black():
            parent.color = NodeColor.BLACK
            sibling.color = NodeColor.RED
            return True
        return False

    def _try_case5(self, node: RBTNode, sibling: RBTNode) -> bool:
        """Handle the near-red-nephew case for a left child.

        If the sibling's left child is red, its right child is black, and
        `node` is the parent's left child, recolor the sibling and its left
        child and perform a right rotation at the sibling.

        Args:
            node: The node whose sibling is to be checked.
            sibling: The sibling to check.

        Returns:
            True if the sibling's left child is red, right child is black, and
            `node` is the left child of its parent; otherwise, False.
        """
        parent = node.parent
        assert parent is not None

        left_child = sibling.left
        right_child = sibling.right

        if (
            left_child is not None
            and left_child.is_red()
            and self._is_none_or_black(right_child)
            and node is parent.left
        ):
            sibling.color = NodeColor.RED
            left_child.color = NodeColor.BLACK
            self._rotate_right(sibling)
            return True
        return False

    def _try_case6(self, node: RBTNode, sibling: RBTNode) -> bool:
        """Handle the near-red-nephew case for a right child.

        If the sibling's right child is red, its left child is black, and
        `node` is the parent's right child, recolor the sibling and its right
        child and perform a left rotation at the sibling.

        Args:
            node: The node whose sibling is to be checked.
            sibling: The sibling to check.

        Returns:
            True if the sibling's left child is black and right child is red, and
            `node` is the right child of its parent; otherwise, False.
        """
        parent = node.parent
        assert parent is not None
        left_child = sibling.left
        right_child = sibling.right

        if (
            right_child is not None
            and right_child.is_red()
            and self._is_none_or_black(left_child)
            and node is parent.right
        ):
            sibling.color = NodeColor.RED
            right_child.color = NodeColor.BLACK
            self._rotate_left(sibling)
            return True
        return False

    def print_tree(self, end: str = "") -> None:
        """Print the tree in a structured format."""
        print(RBTPrint.tree_to_string(self.root), end=end)

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

    def _remove_node(self, node: RBTNode) -> bool:
        """Remove the specified node from the tree.

        Args:
            node: The RBTNode to remove.

        Returns:
            True after the node is removed.
        """
        if node.left is not None and node.right is not None:
            predecessor_node = node.get_predecessor()
            predecessor_key = predecessor_node.key
            self._remove_node(predecessor_node)
            node.key = predecessor_key
            return True

        if node.is_black():
            self._prepare_for_removal(node)
        self._bst_remove_node(node)

        if self.root is not None and self.root.is_red():
            self.root.color = NodeColor.BLACK

        return True

    def _rotate_left(self, node: RBTNode) -> None:
        """Perform a left rotation on the subtree rooted at the given node.

        Args:
            node: The root of the subtree to rotate.
        """
        parent = node.parent
        right_child = node.right
        assert right_child is not None

        transferred_child = right_child.left

        if parent is None:
            self.root = right_child
            right_child.parent = None
        else:
            parent.replace_child(node, right_child)

        right_child.set_left(node)
        node.set_right(transferred_child)

    def _rotate_right(self, node: RBTNode) -> None:
        """Perform a right rotation on the subtree rooted at the given node.

        Args:
            node: The root of the subtree to rotate.
        """
        parent = node.parent
        left_child = node.left
        assert left_child is not None

        transferred_child = left_child.right

        if parent is None:
            self.root = left_child
            left_child.parent = None
        else:
            parent.replace_child(node, left_child)

        left_child.set_right(node)
        node.set_left(transferred_child)

    def search(self, key: int) -> RBTNode | None:
        """Search the tree for a node with the specified key.

        Args:
            key: The key value to locate.

        Returns:
            The RBTNode that contains the key if found; otherwise, None.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(
        self,
        node: RBTNode | None,
        key: int,
    ) -> RBTNode | None:
        """Recursively search the subtree rooted at `node` for `key`.

        Args:
            node: The root of the subtree to search.
            key: The key value to locate.

        Returns:
            The matching RBTNode if found; otherwise, None.
        """
        if node is None:
            return None

        if key == node.key:
            return node

        if key < node.key:
            return self._search_recursive(node.left, key)

        return self._search_recursive(node.right, key)
