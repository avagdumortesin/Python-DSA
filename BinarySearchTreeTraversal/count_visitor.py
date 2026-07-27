from BinarySearchTreeTraversal.bst_node_visitor import BSTNodeVisitor


class CountVisitor(BSTNodeVisitor):
    def __init__(self):
        self.node_count = 0

    def print_summary(self):
        print(f"CountVisitor visited {self.node_count} nodes.")

    def visit(self, node):
        self.node_count += 1
