class HuffmanTreeNode:
    def __init__(self, left_child_node, right_child_node):
        self.left_child = left_child_node
        self.right_child = right_child_node
        self.character = '\0'

        # Compute and assign frequency
        frequency = 0
        if left_child_node is not None:
            frequency += left_child_node.get_frequency()
        if right_child_node is not None:
            frequency += right_child_node.get_frequency()
        self.frequency = frequency

    # Constructs a leaf node with the specified character and frequency
    @staticmethod
    def create_leaf(leaf_character, leaf_frequency):
        new_node = HuffmanTreeNode(None, None)
        new_node.character = leaf_character
        new_node.frequency = leaf_frequency
        return new_node
    def get_character(self):
        return self.character

    # Returns a reference to this node's left child, or None if this node is a leaf
    def get_left_child(self):
        return self.left_child

    # Returns a reference to this node's right child, or None if this node is a leaf
    def get_right_child(self):
        return self.right_child

    # Returns this node's frequency. If this node is a leaf, the frequency is
    # the leaf node's character frequency. If this node is internal, the
    # frequency is the sum of both child frequencies.
    def get_frequency(self):
        return self.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency