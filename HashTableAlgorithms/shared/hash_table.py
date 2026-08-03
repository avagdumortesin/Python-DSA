"""Define the abstract base class for hash-table implementations."""

from abc import ABC, abstractmethod

from HashTableAlgorithms.shared.map_adt import K, MapADT, V


class HashTable(MapADT[K, V], ABC):
    """Abstract base class for hash table implementations."""

    @staticmethod
    def compute_hash(key: K) -> int:
        """Return a non-negative hash code for the specified key."""
        return abs(hash(key))

    @abstractmethod
    def print_table(self) -> None:
        """Print the hash table, including empty buckets."""
        ...
