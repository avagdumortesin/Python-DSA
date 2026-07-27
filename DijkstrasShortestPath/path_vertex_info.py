from __future__ import annotations

from dataclasses import dataclass
from math import inf

from graph_components import Vertex


@dataclass(slots=True)
class PathVertexInfo:
    """Stores shortest-path information for a graph vertex."""

    vertex: Vertex
    distance: float = inf
    predecessor: Vertex | None = None

    @staticmethod
    def remove_min(
        items: list[PathVertexInfo],
    ) -> PathVertexInfo | None:
        """Remove and return the item with the smallest distance.

        Args:
            items: The path information objects to search.

        Returns:
            The item with the minimum distance, or None if the list is empty.
        """
        if not items:
            return None

        min_index = 0

        for index in range(1, len(items)):
            if items[index].distance < items[min_index].distance:
                min_index = index

        return items.pop(min_index)
