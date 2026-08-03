"""Provide a matrix of shortest-path distances between graph vertices."""

import math
from collections.abc import Iterable

from GraphAlgorithms.shared.graph_components import Vertex


class ShortestPathMatrix:
    """Store shortest-path distances for every pair of vertices."""

    def __init__(self, all_vertices: Iterable[Vertex]) -> None:
        """Initialize all vertex-pair distances to infinity."""
        self.vertices: list[Vertex] = sorted(
            all_vertices,
            key=lambda vertex: vertex.label,
        )

        self.matrix: dict[Vertex, dict[Vertex, float]] = {
            from_vertex: {to_vertex: math.inf for to_vertex in self.vertices}
            for from_vertex in self.vertices
        }

    def get(self, from_vertex: Vertex, to_vertex: Vertex) -> float:
        """Return the stored distance between two vertices."""
        return self.matrix[from_vertex][to_vertex]

    def print_matrix(self) -> None:
        """Print the shortest-path distance matrix."""
        print("   ", end="")

        for vertex in self.vertices:
            print(f"  {vertex.label} ", end="")
        print()

        for from_vertex in self.vertices:
            print(f"{from_vertex.label} [ ", end="")

            for to_vertex in self.vertices:
                entry = self.get(from_vertex, to_vertex)

                if entry == math.inf:
                    print("inf ", end="")
                else:
                    if entry >= 0:
                        print(" ", end="")

                    print(f"{int(entry)} ", end="")

                    if -10 < entry < 10:
                        print(" ", end="")

            print("]")

    def set(
        self,
        from_vertex: Vertex,
        to_vertex: Vertex,
        distance: float,
    ) -> None:
        self.matrix[from_vertex][to_vertex] = distance
