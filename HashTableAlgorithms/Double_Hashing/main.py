"""Demonstrate a hash table that resolves collisions through double hashing."""

from double_hashing_hash_table import DoubleHashingHashTable


def main() -> None:
    """Build, display, and modify a hash table through double hashing."""
    keys = [
        "LAX",
        "IAH",
        "IAD",
        "ORD",
        "SFO",
        "DAL",
        "NRT",
        "JFK",
        "YVR",
        "LHR",
    ]
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

    hash_table: DoubleHashingHashTable[str, str] = DoubleHashingHashTable()

    for key, value in zip(keys, values):
        if not hash_table.insert(key, value):
            print(f"ERROR: Could not insert key {key}.")

    print("Buckets:")
    hash_table.print_table()

    keys_to_remove = ["LAX", "ORD"]
    for key in keys_to_remove:
        print(f'\nRemoving "{key}"')

        if not hash_table.remove(key):
            print(f'ERROR: Key "{key}" was not found.')

    print("\nBuckets after removals:")
    hash_table.print_table()


if __name__ == "__main__":
    main()
