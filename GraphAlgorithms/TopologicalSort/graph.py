"""Provides a directed graph supporting topological sorting."""

from GraphAlgorithms.shared.graph_base import GraphBase
from GraphAlgorithms.shared.graph_components import Vertex


class Graph(GraphBase):
    """Represents a directed graph."""

    def topological_sort(self) -> list[Vertex]:
        """Return a topological ordering of the graph's vertices.

        Raises:
            ValueError: If the graph contains a cycle.
        """
        sorted_vertices: list[Vertex] = []

        incoming_count_map: dict[Vertex, int] = {
            vertex: len(edges) for vertex, edges in self.to_edges.items()
        }

        no_incoming_edges: list[Vertex] = [
            vertex for vertex, count in incoming_count_map.items() if count == 0
        ]

        while no_incoming_edges:
            current_vertex = no_incoming_edges.pop()
            sorted_vertices.append(current_vertex)

            for edge in self.get_edges_from(current_vertex):
                to_vertex = edge.to_vertex
                incoming_count_map[to_vertex] -= 1

                if incoming_count_map[to_vertex] == 0:
                    no_incoming_edges.append(to_vertex)

        if len(sorted_vertices) != len(self.from_edges):
            raise ValueError(
                "The graph contains a cycle and cannot be topologically sorted."
            )

        return sorted_vertices
