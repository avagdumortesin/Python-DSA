from __future__ import annotations
from BinarySearchTree.bst_node import BSTNode

class BSTPrint:
    """Utility methods for creating a text representation of a binary search tree.

    This class converts a binary search tree into an ASCII-art representation
    suitable for displaying in a terminal or console window.
    """

    @staticmethod
    def get_spaces(number_of_spaces: int) -> str:
        """Return a string containing the specified number of spaces.

        Args:
            number_of_spaces: The number of spaces to include.

        Returns:
            A string consisting only of space characters.
        """
        return " " * number_of_spaces

    @staticmethod
    def indent_lines(lines: list[str], number_of_spaces: int) -> None:
        """Indent each line in a list by the specified number of spaces.

        Args:
            lines: A list of strings to indent.
            number_of_spaces: The number of leading spaces to add to each line.
        """
        if number_of_spaces > 0:
            # Prepend indentation to each line
            indent = BSTPrint.get_spaces(number_of_spaces)
            for i, line in enumerate(lines):
                lines[i] = indent + line

    @staticmethod
    def tree_to_lines(subtree_root: BSTNode | None) -> list[str]:
        """Convert a binary search tree into a list of printable text lines.

        Args:
            subtree_root: The root node of the subtree to convert.

        Returns:
            A list of strings representing the formatted tree.
        """
        if subtree_root is None:
            return []

        # Make a string with subtree_root's key enclosed in brackets
        node_text = f"[{subtree_root.key}]"
        node_text_len = len(node_text)

        # Case 1: subtree_root is a leaf
        if subtree_root.left is None and subtree_root.right is None:
            return [node_text]

        # Recursively make line strings for each child
        left_lines = BSTPrint.tree_to_lines(subtree_root.left)
        right_lines = BSTPrint.tree_to_lines(subtree_root.right)

        line_count = max(len(left_lines), len(right_lines))
        all_lines = [""] * (line_count + 2)

        # Case 2: subtree_root has no left child
        if subtree_root.left is None:
            # Create the first 2 lines, not yet indented
            all_lines[0] = node_text
            all_lines[1] = BSTPrint.get_spaces(node_text_len) + "\\"
            # Find where the right child starts
            right_child_indent = right_lines[0].find('[')
            # Goal: Indent lines appropriately so that the parent's right
            # branch character ('\') matches up with the right child's '['.
            if right_child_indent <= node_text_len:
                # Indent all lines below
                BSTPrint.indent_lines(right_lines, node_text_len - right_child_indent)
            else:
                # Indent first 2 lines
                indent = BSTPrint.get_spaces(right_child_indent - node_text_len)
                all_lines[0] = indent + all_lines[0]
                all_lines[1] = indent + all_lines[1]
            # Copy right_lines into all_lines starting at index 2
            for i, line in enumerate(right_lines):
                all_lines[i + 2] = line
            return all_lines

        # Case 3: subtree_root has no right child
        if subtree_root.right is None:
            # Goal: Indent lines appropriately so that the parent's left branch
            # character ('/') matches up with the left child's ']'.

            # Create the first 2 lines
            indent = BSTPrint.get_spaces(left_lines[0].find('['))
            all_lines[0] = indent + " " + node_text
            all_lines[1] = indent + "/"

            # Copy left_lines into all_lines starting at index 2
            for i, line in enumerate(left_lines):
                all_lines[i + 2] = line
            return all_lines

        # Case 4: subtree_root has both a left and right child

        # The goal is to have the two child nodes as close to the parent as
        # possible without overlapping on any level.

        # Compute absolute indentation, in number of spaces, needed for right
        # lines
        indent_needed = 0
        if right_lines:
            # Indent should at least get the immediate right child to be to the
            # right of the root
            left0_len = len(left_lines[0])
            indent_needed = max(0, left0_len + len(node_text) -
                                right_lines[0].find('['))

        for i in range(0, min(len(left_lines), len(right_lines)), 2):
            # Lines with branches are skipped, so the line of interest has only
            # nodes. The difference between where the left line ends and the
            # right line begins should be at least 3 spaces for clarity.
            right_begin = right_lines[i].find('[')

            for_this_line = len(left_lines[i]) + 3 - right_begin
            indent_needed = max(indent_needed, for_this_line)

        # Build final lines in all_lines starting at index 2
        absolute_indent = BSTPrint.get_spaces(indent_needed)
        for i in range(0, max(len(left_lines), len(right_lines))):
            # If no right line, just take the left
            if i >= len(right_lines):
                all_lines[2 + i] = left_lines[i]
            else:
                left = ""
                if i < len(left_lines):
                    left = left_lines[i]

                right = absolute_indent + right_lines[i]
                all_lines[2 + i] = left + right[len(left):]

        # The first 2 lines remain. all_lines[2] has the proper string for the
        # 2 child nodes, and so can be used to create branches in all_lines[1].
        left_index = all_lines[2].find(']')
        right_index = all_lines[2].rfind('[')
        all_lines[1] = (
                BSTPrint.get_spaces(left_index)
                + "/"
                + BSTPrint.get_spaces(right_index - left_index - 1)
                + "\\"
        )

        # The space between left_index and right_index is the space that
        # subtree_root's string should occupy. If node_text is too short, put
        # underscores on the sides.
        available_width = right_index - left_index - 1
        if len(node_text) < available_width:
            difference = available_width - len(node_text)
            underscores = "_" * (difference // 2)
            node_text = underscores + node_text + underscores
            if difference % 2 != 0:
                node_text += "_"
        all_lines[0] = BSTPrint.get_spaces(left_index + 1) + node_text
        return all_lines

    @staticmethod
    def tree_to_string(subtree_root: BSTNode | None) -> str:
        """Convert a binary search tree into a printable string.

        Args:
            subtree_root: The root node of the tree.

        Returns:
            A multiline string representing the tree, or "(empty tree)"
            if the tree contains no nodes.
        """
        if subtree_root is None:
            return "(empty tree)"

        # First, convert the tree to a list of line strings
        lines = BSTPrint.tree_to_lines(subtree_root)

        # Combine all lines into one string
        return "\n".join(lines)
