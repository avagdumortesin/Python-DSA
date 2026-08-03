from typing import Protocol

from TreeAlgorithms.BinarySearchTreeTraversal.bst_node import BSTNode


class BSTNodeVisitor(Protocol):
    """Protocol for objects that visit BST nodes during a traversal."""

    def print_summary(self): ...

    def visit(self, node: BSTNode) -> None: ...
