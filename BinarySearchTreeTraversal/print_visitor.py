from BinarySearchTreeTraversal.bst_node_visitor import BSTNodeVisitor

class PrintVisitor(BSTNodeVisitor):
    def print_summary(self):
        print("PrintVisitor is done visiting nodes.")

    def visit(self, node):
        print(f"{node.key} ", end="")