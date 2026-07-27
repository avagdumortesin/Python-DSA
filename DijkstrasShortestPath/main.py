"""Demonstrate Dijkstra's shortest path algorithm."""

from graph import Graph
from graph_components import Vertex
from path_vertex_info import PathVertexInfo


def print_table(
    start_vertex: Vertex,
    vertices: list[Vertex],
    info_map: dict[Vertex, PathVertexInfo],
) -> None:
    """Display the shortest paths from the starting vertex."""
    for vertex in vertices:
        info = info_map[vertex]

        if info.predecessor is None and vertex is not vertices[0]:
            print(f"{start_vertex.label} to {vertex.label}: no path exists")
        else:
            print(
                f"{start_vertex.label} to {vertex.label}: "
                f"{Graph.get_shortest_path(start_vertex, vertex, info_map)} "
                f"(total weight: {int(info.distance)})"
            )

        print()


def main() -> None:
    """Build a weighted graph and demonstrate Dijkstra's algorithm."""
    graph = Graph()

    vertex_a = graph.add_vertex("A")
    vertex_b = graph.add_vertex("B")
    vertex_c = graph.add_vertex("C")
    vertex_d = graph.add_vertex("D")
    vertex_e = graph.add_vertex("E")
    vertex_f = graph.add_vertex("F")
    vertex_g = graph.add_vertex("G")
    vertices = [vertex_a, vertex_b, vertex_c, vertex_d, vertex_e, vertex_f, vertex_g]

    graph.add_undirected_edge(vertex_a, vertex_b, 8)
    graph.add_undirected_edge(vertex_a, vertex_c, 7)
    graph.add_undirected_edge(vertex_a, vertex_d, 3)
    graph.add_undirected_edge(vertex_b, vertex_e, 6)
    graph.add_undirected_edge(vertex_c, vertex_d, 1)
    graph.add_undirected_edge(vertex_c, vertex_e, 2)
    graph.add_undirected_edge(vertex_d, vertex_f, 15)
    graph.add_undirected_edge(vertex_d, vertex_g, 12)
    graph.add_undirected_edge(vertex_e, vertex_f, 4)
    graph.add_undirected_edge(vertex_f, vertex_g, 1)

    # Run Dijkstra's algorithm first
    info_map = graph.dijkstra_shortest_path(vertex_a)

    print_table(vertex_a, vertices, info_map)


if __name__ == "__main__":
    main()
