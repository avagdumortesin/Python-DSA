from AVL.avl_tree import AVLTree


def main() -> None:
    """Demonstrate AVL tree insertion, removal, and printing."""
    # Declare keys to insert and keys to subsequently remove
    keys_to_insert = [10, 20, 5, 22, 15, 47, 19, 3, 12, 18]
    keys_to_remove = [
        12,  # Removing 12 causes a right rotation at node 10
        20,
        30,  # Not in the tree, so remove_key() returns False
    ]

    show_tree_after_each_insertion = False

    # Create an empty AVLTree object
    tree = AVLTree()

    # Insert keys
    for key in keys_to_insert:
        tree.insert_key(key)

        if show_tree_after_each_insertion:
            print(f"Tree after inserting {key}:")
            tree.print_tree("\n\n")

    # Print the tree after all insertions
    print("Tree after initial insertions:")
    tree.print_tree("\n\n")

    # Remove keys
    for key in keys_to_remove:
        if tree.remove_key(key):
            print(f"Removed key {key}:")
            tree.print_tree("\n\n")
        else:
            print(f"Failed to remove key {key} (not found)")


if __name__ == "__main__":
    main()
