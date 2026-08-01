from __future__ import annotations

from dataclasses import dataclass
from typing import Generic

from hash_table import HashTable
from map_adt import K, V


@dataclass(slots=True)
class _ChainingHashTableItem(Generic[K, V]):
    """Represents a single item in a chained hash table."""

    key: K
    value: V
    next: _ChainingHashTableItem[K, V] | None = None


class ChainingHashTable(HashTable[K, V]):
    def __init__(self, initial_capacity: int = 11) -> None:
        self.table: list[_ChainingHashTableItem[K, V] | None] = [
            None
        ] * initial_capacity
        if initial_capacity <= 0:
            raise ValueError("Initial capacity must be greater than zero.")

        self._length = 0

    def bucket_index(self, key: K) -> int:
        """Return the index of the bucket for a given key."""
        return self.compute_hash(key) % len(self.table)

    def contains(self, key: K) -> bool:
        """Check if a key exists in the hash table.

        Args:
            key: The key to search for.

        Returns:
            True if the key exists, False otherwise.
        """
        item = self.table[self.bucket_index(key)]
        while item is not None:
            if item.key == key:
                return True
            item = item.next
        return False

    def __getitem__(self, key: K) -> V:
        """Return the value associated with a key.

        Raises:
            KeyError: If the key does not exist.
        """
        item = self.table[self.bucket_index(key)]

        while item is not None:
            if item.key == key:
                return item.value

            item = item.next

        raise KeyError(key)

    def get_length(self) -> int:
        """Return the length of the hash table."""
        return self._length

    def insert(self, key: K, value: V) -> bool:
        """Insert a key-value pair into the hash table.

        If the key already exists, the value is replaced.

        Args:
            key: The key to insert into the hash table.
            value: The value to insert into the hash table.

        Returns:
            True if the key was inserted or updated; False otherwise.
        """
        bucket_index = self.bucket_index(key)
        current_item = self.table[bucket_index]
        previous_item: _ChainingHashTableItem[K, V] | None = None

        while current_item is not None:
            if current_item.key == key:
                current_item.value = value
                return True

            previous_item = current_item
            current_item = current_item.next

        new_item = _ChainingHashTableItem(key, value)

        if previous_item is None:
            self.table[bucket_index] = new_item
        else:
            previous_item.next = new_item

        self._length += 1
        return True

    def remove(self, key: K) -> bool:
        """Remove a key-value pair from the hash table."""
        bucket_index = self.bucket_index(key)
        current_item = self.table[bucket_index]
        previous_item: _ChainingHashTableItem[K, V] | None = None

        while current_item is not None:
            if key == current_item.key:
                if previous_item is None:
                    self.table[bucket_index] = current_item.next
                else:
                    previous_item.next = current_item.next

                self._length -= 1
                return True

            previous_item = current_item
            current_item = current_item.next

        return False

    def print_map(
        self,
        key_value_separator: str = ": ",
        item_separator: str = ", ",
        prefix: str = "",
        suffix: str = "",
    ) -> None:
        """Print all key-value pairs in the table."""
        formatted_items: list[str] = []

        for bucket in self.table:
            item = bucket

            while item is not None:
                formatted_items.append(f"{item.key}{key_value_separator}{item.value}")
                item = item.next

        print(
            prefix,
            item_separator.join(formatted_items),
            suffix,
            sep="",
            end="",
        )

    def print_table(self) -> None:
        """Print every bucket, including empty buckets."""
        for index, bucket in enumerate(self.table):
            print(f"{index}: ", end="")

            if bucket is None:
                print("(empty)")
                continue

            items: list[str] = []
            current_item = bucket

            while current_item is not None:
                items.append(f"{current_item.key}: {current_item.value}")
                current_item = current_item.next

            print(" --> ".join(items))
