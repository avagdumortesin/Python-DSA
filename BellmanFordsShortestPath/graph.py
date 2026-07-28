"""Provides a weighted digraph for Bellman-Ford's shortest path algorithm."""

from graph_components import Edge, Vertex
from path_vertex_info import PathVertexInfo


class Graph:
    """Represents a weighted digraph."""

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

    def bellman_ford_shortest_path(
        self, start_vertex: Vertex
    ) -> tuple[bool, dict[Vertex, PathVertexInfo]]:
        """Compute shortest paths using the Bellman-Ford algorithm.

        Args:
            start_vertex: The vertex from which distances are calculated.

        Returns:
            A tuple containing whether no reachable negative-weight cycle was
            detected and a mapping of vertices to their path information.

        Raises:
            ValueError: If the starting vertex is not part of the graph.
        """
        if start_vertex not in self.from_edges:
            raise ValueError("The starting vertex is not part of this graph.")

        info: dict[Vertex, PathVertexInfo] = {
            vertex: PathVertexInfo(vertex=vertex) for vertex in self.from_edges
        }
        info[start_vertex].distance = 0.0

        edges = self.get_edges()

        for _ in range(len(info) - 1):
            updated = False

            for edge in edges:
                current_info = info[edge.from_vertex]
                neighbor_info = info[edge.to_vertex]

                candidate_distance = current_info.distance + edge.weight

                if candidate_distance < neighbor_info.distance:
                    neighbor_info.distance = candidate_distance
                    neighbor_info.predecessor = edge.from_vertex
                    updated = True

            if not updated:
                break

        for edge in edges:
            current_info = info[edge.from_vertex]
            neighbor_info = info[edge.to_vertex]

            if current_info.distance + edge.weight < neighbor_info.distance:
                return False, info

        return True, info

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

    @staticmethod
    def get_shortest_path(
        start_vertex: Vertex,
        end_vertex: Vertex,
        info_map: dict[Vertex, PathVertexInfo],
    ) -> str:
        """Return the shortest path between two vertices as a formatted string.

        Raises:
            ValueError: If no path exists between the vertices.
        """
        path = [end_vertex.label]
        current_vertex = end_vertex

        while current_vertex is not start_vertex:
            predecessor = info_map[current_vertex].predecessor

            if predecessor is None:
                raise ValueError(
                    f"No path exists from {start_vertex.label} to {end_vertex.label}."
                )

            current_vertex = predecessor
            path.append(current_vertex.label)

        return " -> ".join(reversed(path))

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
