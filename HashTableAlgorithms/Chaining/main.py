"""Demonstrate a hash table that resolves collisions through chaining."""

from chaining_hash_table import ChainingHashTable


def main() -> None:
    """Build, display, and modify a chaining hash table."""
    keys = ["LAX", "IAH", "IAD", "ORD", "SFO", "DAL", "NRT", "JFK", "YVR", "LHR"]
    values = [
        "Los Angeles",
        "Houston",
        "Washington",
        "Chicago",
        "San Francisco",
        "Dallas",
        "Tokyo",
        "New York",
        "Vancouver",
        "London",
    ]

    hash_table: ChainingHashTable[str, str] = ChainingHashTable()

    for key, value in zip(keys, values):
        hash_table.insert(key, value)

    print("Items: ")
    hash_table.print_map(
        key_value_separator=": ",
        item_separator="\n",
        suffix="\n",
    )

    print("\nBuckets:")
    hash_table.print_table()

    keys_to_remove = ["LAX", "ORD"]
    for key in keys_to_remove:
        print(f'\nRemoving "{key}"')
        hash_table.remove(key)

    print("\nBuckets after removals:")
    hash_table.print_table()


if __name__ == "__main__":
    main()
