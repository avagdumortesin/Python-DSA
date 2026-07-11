import heapq
from huffman_tree_node import HuffmanTreeNode
from huffman_compressed_string import HuffmanCompressedString

class Huffman:

    @staticmethod
    def build_frequency_table(input_string):
        table = dict()
        for string_char in input_string:
            if string_char in table:
                table[string_char] = table[string_char] + 1
            else:
                table[string_char] = 1
        return table

    @staticmethod
    def build_tree(input_string: str) -> HuffmanTreeNode:
        # First build the frequency table
        table = Huffman.build_frequency_table(input_string)

        # Make a priority queue of nodes
        nodes: list[HuffmanTreeNode] = []
        for character in table:
            new_leaf = HuffmanTreeNode.create_leaf(character, table[character])
            heapq.heappush(nodes,new_leaf)

        # Make parent nodes up to the root
        while len(nodes) > 1:
            # Dequeue two lowest priority nodes
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)

            # Enqueue parent back into priority queue
            heapq.heappush(nodes, HuffmanTreeNode(left, right))

        return heapq.heappop(nodes)

    @staticmethod
    def get_codes(node, prefix, output):
        if node.get_left_child() is None:
            output[node.get_character()] = prefix
        else:
            left = node.get_left_child()
            Huffman.get_codes(left, prefix + "0", output)
            right = node.get_right_child()
            Huffman.get_codes(right, prefix + "1", output)

    @staticmethod
    def compress(input_string):
        if 0 == len(input_string):
            return None

        # Build the Huffman tree
        root = Huffman.build_tree(input_string)

        # Get the compression codes from the tree
        codes = dict()
        Huffman.get_codes(root, "", codes)

        # Build the compressed result
        result = ""
        for c in input_string:
            result += codes[c]
        return HuffmanCompressedString(input_string, result, root)

    @staticmethod
    def decompress(compressed_string, tree_root):
        node = tree_root
        result = ""
        for bit_char in compressed_string:
            # Go left or right based on bit_char value
            if '0' == bit_char:
                node = node.get_left_child()
            else:
                node = node.get_right_child()

            # If the node is a leaf, add the character to the decompressed
            # result and go back to the root node
            if node.get_left_child() is None:
                result += node.get_character()
                node = tree_root

        return result
