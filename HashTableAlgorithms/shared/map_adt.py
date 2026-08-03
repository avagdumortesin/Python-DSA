"""Define the abstract interface for map implementations."""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class MapADT(ABC, Generic[K, V]):
    """Define the operations supported by a map data structure."""

    @abstractmethod
    def contains(self, key: K) -> bool:
        """Return whether the specified key exists in the map."""
        ...

    @abstractmethod
    def __getitem__(self, key: K) -> V:
        """Return the value associated with a key.

        Raises:
            KeyError: If the key does not exist in the map.
        """
        ...

    def get(self, key: K, default: V | None = None) -> V | None:
        """Return the associated value or a default if the key is absent."""
        try:
            return self[key]
        except KeyError:
            return default

    @abstractmethod
    def get_length(self) -> int:
        """Return the number of key-value pairs in the map."""
        ...

    @abstractmethod
    def insert(self, key: K, value: V) -> bool:
        """Insert or update a key-value pair."""
        ...

    @abstractmethod
    def print_map(
        self,
        key_value_separator: str = ":",
        item_separator: str = ", ",
        prefix: str = "",
        suffix: str = "",
    ) -> None:
        """Print all key-value pairs in the map."""
        ...

    @abstractmethod
    def remove(self, key: K) -> bool:
        """Remove the item associated with a key, if present."""
        ...
