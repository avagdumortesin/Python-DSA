"""Provide a disjoint-set collection for Kruskal's algorithm."""

from GraphAlgorithms.shared.graph_components import Vertex


class VertexSetCollection:
    """Manage disjoint sets of graph vertices."""

    def __init__(self, all_vertices: list[Vertex]) -> None:
        """Initialize each vertex in its own set."""
        self.vertex_map: dict[Vertex, set[Vertex]] = {
            vertex: {vertex} for vertex in all_vertices
        }

    def get_set(self, vertex: Vertex) -> set[Vertex]:
        """Return the set containing the given vertex."""
        return self.vertex_map[vertex]

    def merge(
        self,
        vertex_set_1: set[Vertex],
        vertex_set_2: set[Vertex],
    ) -> bool:
        """Merge two distinct vertex sets.

        Returns:
            True if the sets were merged, False if they were already the same set.
        """
        if vertex_set_1 is vertex_set_2:
            return False

        merged_set = vertex_set_1.union(vertex_set_2)

        for vertex in merged_set:
            self.vertex_map[vertex] = merged_set

        return True
