from BinarySearchTreeTraversal.bst_node_visitor import BSTNodeVisitor

class ListVisitor(BSTNodeVisitor):
    def __init__(self):
        self.visited_nodes = []

    def print_summary(self):
        print(f"ListVisitor visited {len(self.visited_nodes)} nodes: ", end="")
        for node in self.visited_nodes:
            print(f"{node.key} ", end="")
        print()

    def visit(self, node):
        self.visited_nodes.append(node)