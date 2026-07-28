"""Provides a directed graph supporting topological sorting."""

from graph_components import Edge, Vertex


class Graph:
    """Represents a directed graph."""

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
