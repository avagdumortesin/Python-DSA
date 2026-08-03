from red_black_tree import RedBlackTree


def main() -> None:
    """Demonstrate red-black tree insertion and removal."""
    keys_to_insert = [10, 20, 5, 22, 15, 47, 19, 3, 12, 18]
    keys_to_remove = [
        12,  # Removing 12 causes a right rotation at node 10
        20,
        30,  # 30 is not in the tree, so remove_key() will return False
    ]

    show_tree_after_each_insertion = False
    tree = RedBlackTree()

    # Insert keys
    for key in keys_to_insert:
        tree.insert_key(key)

        if show_tree_after_each_insertion:
            print(f"Tree after inserting {key}:")
            tree.print_tree(end="\n\n")

    print("Tree after initial insertions:")
    tree.print_tree(end="\n\n")
    print()

    # Remove keys
    for key in keys_to_remove:
        if tree.remove_key(key):
            print(f"Tree after removing {key}:")
            tree.print_tree(end="\n\n")
        else:
            print(f"Failed to remove key {key} (not found)")


if __name__ == "__main__":
    main()
