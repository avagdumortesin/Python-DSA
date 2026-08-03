"""Provides a directed graph with breadth-first traversal."""

from collections import deque

from bfs_visitors import VertexVisitor

from GraphAlgorithms.shared.graph_base import GraphBase
from GraphAlgorithms.shared.graph_components import Vertex


class Graph(GraphBase):
    """Represents a weighted directed graph."""

    def breadth_first_search(
        self,
        start_vertex: Vertex,
        visitor: VertexVisitor,
        distances: dict[Vertex, int],
    ) -> None:
        """Traverse the graph breadth-first from the specified vertex."""
        discovered: set[Vertex] = {start_vertex}
        frontier: deque[Vertex] = deque([start_vertex])

        distances[start_vertex] = 0

        while frontier:
            current_vertex = frontier.popleft()
            visitor.visit(current_vertex)

            for edge in self.get_edges_from(current_vertex):
                adjacent_vertex = edge.to_vertex

                if adjacent_vertex not in discovered:
                    frontier.append(adjacent_vertex)
                    discovered.add(adjacent_vertex)
                    distances[adjacent_vertex] = distances[current_vertex] + 1
