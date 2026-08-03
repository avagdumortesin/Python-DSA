from TreeAlgorithms.BinarySearchTreeTraversal.binary_search_tree import BinarySearchTree
from TreeAlgorithms.BinarySearchTreeTraversal.count_visitor import CountVisitor
from TreeAlgorithms.BinarySearchTreeTraversal.list_visitor import ListVisitor
from TreeAlgorithms.BinarySearchTreeTraversal.print_visitor import PrintVisitor


def main():
    # The following values are inserted to build the tree
    keys_to_insert = [83, 25, 76, 67, 88, 12, 19, 54, 26, 73, 23, 44, 81]

    # Create a tree
    tree = BinarySearchTree()

    # Insert keys
    for key in keys_to_insert:
        tree.insert_key(key)

    # Create one of each visitor
    visitors = [PrintVisitor(), CountVisitor(), ListVisitor()]

    # Perform an inorder traversal with each visitor and print a summary
    for visitor in visitors:
        tree.in_order_traversal(visitor)
        visitor.print_summary()
        print()


if __name__ == "__main__":
    main()
