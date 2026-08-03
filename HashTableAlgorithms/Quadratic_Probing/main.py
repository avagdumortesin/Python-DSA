"""Demonstrate a hash table that resolves collisions through quadratic-probing."""

from quadratic_probing_hash_table import QuadraticProbingHashTable


def main() -> None:
    """Build, display, and modify a quadratic-probing hash table."""
    keys = [
        "LAX",
        "IAH",
        "IAD",
        "ORD",
        "SFO",
        "DAL",
        "NRT",
        "JFK",
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
    ]

    hash_table: QuadraticProbingHashTable[str, str] = QuadraticProbingHashTable()

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
