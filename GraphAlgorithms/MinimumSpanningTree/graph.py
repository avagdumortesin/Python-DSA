"""Provide a weighted graph supporting Kruskal's algorithm."""

from vertex_set_collection import VertexSetCollection

from GraphAlgorithms.shared.graph_base import GraphBase
from GraphAlgorithms.shared.graph_components import Edge


class Graph(GraphBase):
    """Represent a weighted graph supporting Kruskal's algorithm."""

    def minimum_spanning_tree(self) -> list[Edge]:
        """Return the minimum spanning tree of the graph."""
        edges = sorted(self.get_edges(), key=lambda current_edge: current_edge.weight)

        vertex_sets = VertexSetCollection(self.get_vertices())
        result: list[Edge] = []
        for edge in edges:
            set_1 = vertex_sets.get_set(edge.from_vertex)
            set_2 = vertex_sets.get_set(edge.to_vertex)

            if vertex_sets.merge(set_1, set_2):
                result.append(edge)

        return result
