from binary_search_tree import BinarySearchTree
from bst_print import BSTPrint

def main():
    # The following values are inserted in this order to build the tree
    values_to_insert = [3, 10, 7, 2, 8, 4, 9, 5, 1, 6]

    # Then the following values are removed from the tree
    values_to_remove = [5, 3]

    tree = BinarySearchTree()

    # Insert values
    for value in values_to_insert:
        tree.insert_key(value)

    # Show the tree
    print("Initial tree:")
    print(BSTPrint.tree_to_string(tree.get_root()))

    # Remove values
    for value_to_remove in values_to_remove:
        print()
        if tree.remove(value_to_remove):
            print(f"Tree after removing {value_to_remove}:")
            print(BSTPrint.tree_to_string(tree.get_root()))
        else:
            print(f"Key {value_to_remove} not found")

if __name__ == "__main__":
    main()