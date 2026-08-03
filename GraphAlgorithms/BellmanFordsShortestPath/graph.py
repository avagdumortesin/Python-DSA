"""Provides a weighted digraph for Bellman-Ford's shortest path algorithm."""

from path_vertex_info import PathVertexInfo

from GraphAlgorithms.shared.graph_base import GraphBase
from GraphAlgorithms.shared.graph_components import Vertex


class Graph(GraphBase):
    """Represents a weighted digraph."""

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
