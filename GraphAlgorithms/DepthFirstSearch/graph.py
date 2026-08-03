"""Provides a directed graph with depth-first traversal."""

from dfs_visitors import VertexVisitor

from GraphAlgorithms.shared.graph_base import GraphBase
from GraphAlgorithms.shared.graph_components import Vertex


class Graph(GraphBase):
    """Represents a weighted directed graph."""

    def depth_first_search(
        self,
        start_vertex: Vertex,
        visitor: VertexVisitor,
    ) -> None:
        """Visit each reachable vertex using depth-first traversal."""
        vertex_stack: list[Vertex] = [start_vertex]
        visited_set: set[Vertex] = set()

        while vertex_stack:
            current_vertex = vertex_stack.pop()

            if current_vertex in visited_set:
                continue

            visitor.visit(current_vertex)
            visited_set.add(current_vertex)

            for edge in self.get_edges_from(current_vertex):
                vertex_stack.append(edge.to_vertex)
