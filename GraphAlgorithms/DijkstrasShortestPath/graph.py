"""Provide a weighted graph supporting Dijkstra's algorithm."""

from path_vertex_info import PathVertexInfo

from GraphAlgorithms.shared.graph_base import GraphBase
from GraphAlgorithms.shared.graph_components import Vertex


class Graph(GraphBase):
    """Represent a weighted graph supporting Dijkstra's algorithm."""

    def dijkstra_shortest_path(
        self, start_vertex: Vertex
    ) -> dict[Vertex, PathVertexInfo]:
        """Compute shortest paths from a starting vertex to all other vertices."""
        if start_vertex not in self.from_edges:
            raise ValueError("The starting vertex is not part of this graph.")

        if any(edge.weight < 0 for edge in self.get_edges()):
            raise ValueError("Dijkstra's algorithm requires nonnegative edge weights.")

        path_info: dict[Vertex, PathVertexInfo] = {
            vertex: PathVertexInfo(vertex=vertex) for vertex in self.from_edges
        }
        path_info[start_vertex].distance = 0

        unvisited_vertices: list[PathVertexInfo] = list(path_info.values())

        while unvisited_vertices:
            current_info = PathVertexInfo.remove_min(unvisited_vertices)
            if current_info is None:
                break

            current_vertex = current_info.vertex

            for edge in self.get_edges_from(current_vertex):
                neighbor_vertex = edge.to_vertex
                neighbor_info = path_info[neighbor_vertex]

                candidate_distance = current_info.distance + edge.weight
                if candidate_distance < neighbor_info.distance:
                    neighbor_info.distance = candidate_distance
                    neighbor_info.predecessor = current_vertex

        return path_info

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
