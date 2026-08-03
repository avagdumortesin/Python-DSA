"""Provides a weighted graph supporting the Floyd-Warshall algorithm."""

import math

from shortest_path_matrix import ShortestPathMatrix

from GraphAlgorithms.shared.graph_base import GraphBase
from GraphAlgorithms.shared.graph_components import Edge, Vertex


class Graph(GraphBase):
    """Represents a weighted graph."""

    def all_pairs_shortest_path(self) -> ShortestPathMatrix:
        """Return the all-pairs shortest-path distance matrix."""
        all_vertices = self.get_vertices()
        all_edges = self.get_edges_list()

        dist_matrix = ShortestPathMatrix(all_vertices)

        for vertex in all_vertices:
            dist_matrix.set(vertex, vertex, 0.0)

        for edge in all_edges:
            dist_matrix.set(edge.from_vertex, edge.to_vertex, edge.weight)

        for k_vertex in all_vertices:
            for from_vertex in all_vertices:
                for to_vertex in all_vertices:
                    current_length = dist_matrix.get(from_vertex, to_vertex)
                    possible_length = dist_matrix.get(
                        from_vertex, k_vertex
                    ) + dist_matrix.get(k_vertex, to_vertex)
                    if possible_length < current_length:
                        dist_matrix.set(from_vertex, to_vertex, possible_length)

        return dist_matrix

    def reconstruct_path(
        self,
        from_vertex: Vertex,
        to_vertex: Vertex,
        dist_matrix: ShortestPathMatrix,
    ) -> list[Edge]:
        """Reconstruct the shortest path from one vertex to another using the
        distance matrix."""
        if math.isinf(dist_matrix.get(from_vertex, to_vertex)):
            return []

        path = []
        current_vertex = to_vertex

        while current_vertex is not from_vertex:
            incoming_edges = self.get_edges_to(current_vertex)

            for current_edge in incoming_edges:
                expected = (
                    dist_matrix.get(from_vertex, current_vertex) - current_edge.weight
                )
                actual = dist_matrix.get(from_vertex, current_edge.from_vertex)

                if expected == actual:
                    current_vertex = current_edge.from_vertex
                    path.append(current_edge)
                    break

        return list(reversed(path))
