from __future__ import annotations

from typing import ClassVar, Generic

from HashTableAlgorithms.shared.map_adt import K, V


class OpenAddressingBucket(Generic[K, V]):
    """Represent one bucket in an open-addressing hash table."""

    EMPTY_SINCE_START: ClassVar[OpenAddressingBucket]
    EMPTY_AFTER_REMOVAL: ClassVar[OpenAddressingBucket]

    def __init__(
        self,
        bucket_key: K | None = None,
        bucket_value: V | None = None,
    ) -> None:
        self.key = bucket_key
        self.value = bucket_value

    def is_empty(self) -> bool:
        """Return whether the bucket is empty."""
        return (
            self is OpenAddressingBucket.EMPTY_SINCE_START
            or self is OpenAddressingBucket.EMPTY_AFTER_REMOVAL
        )

    def is_empty_after_removal(self) -> bool:
        """Return whether the bucket was emptied by removal."""
        return self is OpenAddressingBucket.EMPTY_AFTER_REMOVAL

    def is_empty_since_start(self) -> bool:
        """Return whether the bucket has never contained an item."""
        return self is OpenAddressingBucket.EMPTY_SINCE_START


OpenAddressingBucket.EMPTY_SINCE_START = OpenAddressingBucket()
OpenAddressingBucket.EMPTY_AFTER_REMOVAL = OpenAddressingBucket()
