from AVL.avl_node import AVLNode


class AVLPrint:
    """Utility methods for creating a text representation of an AVL tree.

    This class converts an AVL tree into an ASCII-art representation
    suitable for displaying in a terminal or console window.
    """

    @staticmethod
    def _get_spaces(number_of_spaces: int) -> str:
        """Return a string containing the specified number of spaces.

        Args:
            number_of_spaces: The number of spaces to include.

        Returns:
            A string consisting only of space characters.
        """
        return " " * number_of_spaces

    @staticmethod
    def _indent_lines(lines: list[str], number_of_spaces: int) -> None:
        """Indent each line in a list by the specified number of spaces.

        Args:
            lines: A list of strings to indent.
            number_of_spaces: The number of leading spaces to add to each line.
        """
        if number_of_spaces > 0:
            indent = AVLPrint._get_spaces(number_of_spaces)
            for i, line in enumerate(lines):
                lines[i] = indent + line

    @staticmethod
    def tree_to_lines(subtree_root: AVLNode | None) -> list[str]:
        """Convert an AVL tree into a list of printable text lines.

        Args:
            subtree_root: The root node of the subtree to convert.

        Returns:
            A list of strings representing the formatted tree.
        """
        if subtree_root is None:
            return []

        # Display the current node enclosed in brackets.
        node_text = f"[{subtree_root.key}]"
        node_text_len = len(node_text)

        # Leaf node
        if subtree_root.left is None and subtree_root.right is None:
            return [node_text]

        # Recursively render the child subtrees.
        left_lines = AVLPrint.tree_to_lines(subtree_root.left)
        right_lines = AVLPrint.tree_to_lines(subtree_root.right)

        line_count = max(len(left_lines), len(right_lines))
        all_lines = [""] * (line_count + 2)

        # No left child
        if subtree_root.left is None:
            # Build the node and connecting branch.
            all_lines[0] = node_text
            all_lines[1] = AVLPrint._get_spaces(node_text_len) + "\\"
            # Locate the start of the rendered right subtree.
            right_child_indent = right_lines[0].find("[")
            # Align the branch with the right child's opening bracket.
            if right_child_indent <= node_text_len:
                # Shift the right subtree.
                AVLPrint._indent_lines(right_lines, node_text_len - right_child_indent)
            else:
                # Shift the current node instead.
                indent = AVLPrint._get_spaces(right_child_indent - node_text_len)
                all_lines[0] = indent + all_lines[0]
                all_lines[1] = indent + all_lines[1]
            # Append the rendered right subtree.
            for i, line in enumerate(right_lines):
                all_lines[i + 2] = line
            return all_lines

        # No right child
        if subtree_root.right is None:
            # Align the branch with the left child's closing bracket.
            indent = AVLPrint._get_spaces(left_lines[0].find("]"))
            all_lines[0] = indent + " " + node_text
            all_lines[1] = indent + "/"

            # Append the rendered left subtree.
            for i, line in enumerate(left_lines):
                all_lines[i + 2] = line
            return all_lines

        # Two children

        # Position the child subtrees as close together as possible without
        # overlapping.

        # Shift the right subtree far enough to begin beyond the current node.
        indent_needed = max(
            0,
            len(left_lines[0]) + len(node_text) - right_lines[0].find("["),
        )

        for i in range(0, min(len(left_lines), len(right_lines)), 2):
            # Compare only node rows and keep at least three spaces between the
            # rendered left and right subtrees.
            right_begin = right_lines[i].find("[")

            for_this_line = len(left_lines[i]) + 3 - right_begin
            indent_needed = max(indent_needed, for_this_line)

        # Merge the rendered left and right subtrees.
        absolute_indent = AVLPrint._get_spaces(indent_needed)
        for i in range(max(len(left_lines), len(right_lines))):
            # Only the left subtree has remaining lines.
            if i >= len(right_lines):
                all_lines[2 + i] = left_lines[i]
            else:
                left = ""
                if i < len(left_lines):
                    left = left_lines[i]

                right = absolute_indent + right_lines[i]
                all_lines[2 + i] = left + right[len(left) :]

        # Use the child positions to draw the connecting branches.
        left_index = all_lines[2].find("]")
        right_index = all_lines[2].rfind("[")
        all_lines[1] = (
            AVLPrint._get_spaces(left_index)
            + "/"
            + AVLPrint._get_spaces(right_index - left_index - 1)
            + "\\"
        )

        # Pad the node label with underscores if it is narrower than the
        # available space.
        available_width = right_index - left_index - 1
        if len(node_text) < available_width:
            difference = available_width - len(node_text)
            underscores = "_" * (difference // 2)
            node_text = underscores + node_text + underscores
            if difference % 2 != 0:
                node_text += "_"
        all_lines[0] = AVLPrint._get_spaces(left_index + 1) + node_text
        return all_lines

    @staticmethod
    def tree_to_string(subtree_root: AVLNode | None) -> str:
        """Convert an AVL tree into a printable string.

        Args:
            subtree_root: The root node of the tree.

        Returns:
            A multiline string representing the tree, or "(empty tree)"
            if the tree contains no nodes.
        """
        if subtree_root is None:
            return "(empty tree)"

        lines = AVLPrint.tree_to_lines(subtree_root)
        return "\n".join(lines)
