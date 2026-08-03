"""Implement a hash table using quadratic-probing."""

from __future__ import annotations

from hash_table import HashTable
from map_adt import K, V
from open_addressing_bucket import OpenAddressingBucket


def _format_value(value: object) -> str:
    """Return a string representation of a value for display purposes."""
    return str(value)


class QuadraticProbingHashTable(HashTable[K, V]):
    """Implement an open-addressing hash table with quadratic-probing."""

    def __init__(
        self,
        c1: int = 1,
        c2: int = 1,
        initial_capacity: int = 13,
    ) -> None:
        if initial_capacity <= 0:
            raise ValueError("Initial capacity must be greater than zero.")
        if c1 == 0 and c2 == 0:
            raise ValueError("At least one probing coefficient must be nonzero.")
        self.table: list[OpenAddressingBucket[K, V]] = [
            OpenAddressingBucket.EMPTY_SINCE_START
        ] * initial_capacity
        self.c1: int = c1
        self.c2: int = c2

        self._length: int = 0

    def bucket_index(self, key: K, offset: int = 0) -> int:
        """Return the bucket index for a quadratic-probing offset."""
        return (
            self.compute_hash(key) + self.c1 * offset + self.c2 * offset * offset
        ) % len(self.table)

    def contains(self, key: K) -> bool:
        """Check if a key exists in the hash table.

        Args:
            key: The key to search for.

        Returns:
            True if the key exists, False otherwise.
        """
        for offset in range(len(self.table)):
            bucket_index = self.bucket_index(key, offset)
            bucket = self.table[bucket_index]

            if bucket.is_empty_since_start():
                return False

            if not bucket.is_empty_after_removal() and bucket.key == key:
                return True

        return False

    def __getitem__(self, key: K) -> V:
        """Return the value associated with a key.

        Raises:
            KeyError: If the key does not exist.
        """
        for offset in range(len(self.table)):
            bucket_index = self.bucket_index(key, offset)
            bucket = self.table[bucket_index]

            if bucket.is_empty_since_start():
                raise KeyError(key)

            if not bucket.is_empty_after_removal() and bucket.key == key:
                return bucket.value

        raise KeyError(key)

    def get_length(self) -> int:
        """Return the number of key-value pairs stored in the table."""
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
        first_available_index: int | None = None

        for offset in range(len(self.table)):
            bucket_index = self.bucket_index(key, offset)
            bucket = self.table[bucket_index]

            if bucket.is_empty_after_removal():
                first_available_index = (
                    bucket_index
                    if first_available_index is None
                    else first_available_index
                )
                continue

            if bucket.is_empty_since_start():
                insertion_index = (
                    first_available_index
                    if first_available_index is not None
                    else bucket_index
                )
                self.table[insertion_index] = OpenAddressingBucket(key, value)
                self._length += 1
                return True

            if bucket.key == key:
                bucket.value = value
                return True

        if first_available_index is not None:
            self.table[first_available_index] = OpenAddressingBucket(key, value)
            self._length += 1
            return True

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
            if bucket.is_empty():
                continue

            formatted_items.append(
                f"{_format_value(bucket.key)}"
                f"{key_value_separator}"
                f"{_format_value(bucket.value)}"
            )

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

            if bucket.is_empty_since_start():
                print("EMPTY_SINCE_START")
            elif bucket.is_empty_after_removal():
                print("EMPTY_AFTER_REMOVAL")
            else:
                print(f"{_format_value(bucket.key)}: {_format_value(bucket.value)}")

    def remove(self, key: K) -> bool:
        """Remove a key-value pair from the hash table."""
        for offset in range(len(self.table)):
            bucket_index = self.bucket_index(key, offset)
            bucket = self.table[bucket_index]

            if bucket.is_empty_since_start():
                return False

            if not bucket.is_empty_after_removal() and bucket.key == key:
                self.table[bucket_index] = OpenAddressingBucket.EMPTY_AFTER_REMOVAL
                self._length -= 1
                return True

        return False
