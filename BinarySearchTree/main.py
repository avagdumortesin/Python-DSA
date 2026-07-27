from BinarySearchTree.binary_search_tree import BinarySearchTree
from BinarySearchTree.bst_print import BSTPrint


def main() -> None:
    """Demonstrate insertion and removal in a binary search tree."""
    # The following values are inserted in this order to build the tree
    values_to_insert = [3, 10, 7, 2, 8, 4, 9, 5, 1, 6]

    # Then the following values are removed from the tree
    values_to_remove = [5, 3]

    tree = BinarySearchTree()

    for value in values_to_insert:
        tree.insert_key(value)

    print("Initial tree:")
    print(BSTPrint.tree_to_string(tree.root))

    for value in values_to_remove:
        print()
        if tree.remove_key(value):
            print(f"Tree after removing {value}:")
            print(BSTPrint.tree_to_string(tree.root))
        else:
            print(f"Key {value} not found")


if __name__ == "__main__":
    main()
