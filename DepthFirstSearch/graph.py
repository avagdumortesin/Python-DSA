"""Provides a directed graph with depth-first traversal."""

from dfs_visitors import VertexVisitor
from graph_components import Edge, Vertex


class Graph:
    """Represents a weighted directed graph."""

    def __init__(self) -> None:
        """Initialize an empty graph."""
        self.from_edges: dict[Vertex, list[Edge]] = {}
        self.to_edges: dict[Vertex, list[Edge]] = {}

    def add_vertex(self, vertex_label: str) -> Vertex:
        """Add and return a vertex with the specified label."""
        new_vertex = Vertex(vertex_label)
        self.from_edges[new_vertex] = []
        self.to_edges[new_vertex] = []
        return new_vertex

    def add_directed_edge(
        self,
        from_vertex: Vertex,
        to_vertex: Vertex,
        weight: float = 1.0,
    ) -> Edge | None:
        """Add a directed edge unless the edge already exists."""
        if self.has_edge(from_vertex, to_vertex):
            return None

        new_edge = Edge(from_vertex, to_vertex, weight)
        self.from_edges[from_vertex].append(new_edge)
        self.to_edges[to_vertex].append(new_edge)

        return new_edge

    def add_undirected_edge(
        self,
        vertex_1: Vertex,
        vertex_2: Vertex,
        weight: float = 1.0,
    ) -> tuple[Edge | None, Edge | None]:
        """Add directed edges in both directions between two vertices."""
        edge_1 = self.add_directed_edge(vertex_1, vertex_2, weight)
        edge_2 = self.add_directed_edge(vertex_2, vertex_1, weight)
        return edge_1, edge_2

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

    def get_edges(self) -> set[Edge]:
        """Return all distinct edges in the graph."""
        return {edge for edges in self.from_edges.values() for edge in edges}

    def get_edges_from(self, from_vertex: Vertex) -> list[Edge]:
        """Return the edges originating from a vertex."""
        return self.from_edges[from_vertex]

    def get_edges_list(self) -> list[Edge]:
        """Return all distinct edges as a list."""
        return list(self.get_edges())

    def get_edges_to(self, to_vertex: Vertex) -> list[Edge]:
        """Return the edges terminating at a vertex."""
        return self.to_edges[to_vertex]

    def get_vertex(self, vertex_label: str) -> Vertex | None:
        """Return the vertex with the specified label, if present."""
        for vertex in self.from_edges:
            if vertex.label == vertex_label:
                return vertex
        return None

    def get_vertices(self) -> list[Vertex]:
        """Return all vertices in the graph."""
        return list(self.from_edges)

    def has_edge(
        self,
        from_vertex: Vertex,
        to_vertex: Vertex,
    ) -> bool:
        """Return whether a directed edge connects two vertices."""
        if from_vertex not in self.from_edges:
            return False

        return any(edge.to_vertex is to_vertex for edge in self.from_edges[from_vertex])
