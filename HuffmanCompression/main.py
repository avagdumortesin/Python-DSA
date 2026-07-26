"""Demonstrate Huffman compression and decompression."""

from huffman import Huffman


def main() -> None:
    """Compress a sample message, restore it, and display the results."""
    message = "the quick brown fox jumps over the lazy dog"

    compressed_data = Huffman.compress(message)
    if compressed_data is None:
        print("The input string is empty and cannot be compressed.")
        return

    restored_message = Huffman.decompress(
        compressed_data.compressed,
        compressed_data.root,
    )

    original_bits = len(message.encode("utf-8")) * 8
    compressed_bits = len(compressed_data.compressed)
    bits_saved = original_bits - compressed_bits
    reduction = bits_saved / original_bits * 100

    print("Huffman compression demonstration:")
    print(f"Original message:   {message}")
    print(f"Compressed data:    {compressed_data.compressed}")
    print(f"Restored message:   {restored_message}")
    print()
    print(f"Original size:      {original_bits} bits")
    print(f"Compressed size:    {compressed_bits} bits")
    print(f"Space reduction:    {reduction:.2f}%")
    print(f"Successful restore: {restored_message == message}")


if __name__ == "__main__":
    main()