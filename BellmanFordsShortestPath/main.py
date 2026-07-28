"""Demonstrate the Bellman-Ford shortest path algorithm."""

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

        if info.predecessor is None and vertex is not start_vertex:
            print(f"{start_vertex.label} to {vertex.label}: no path exists")
        else:
            print(
                f"{start_vertex.label} to {vertex.label}: "
                f"{Graph.get_shortest_path(start_vertex, vertex, info_map)} "
                f"(total weight: {int(info.distance)})"
            )

        print()


def main() -> None:
    """Build a weighted graph and demonstrate the Bellman-Ford algorithm."""
    graph = Graph()

    vertex_a = graph.add_vertex("A")
    vertex_b = graph.add_vertex("B")
    vertex_c = graph.add_vertex("C")
    vertex_d = graph.add_vertex("D")
    vertex_e = graph.add_vertex("E")
    vertex_f = graph.add_vertex("F")
    vertices = [vertex_a, vertex_b, vertex_c, vertex_d, vertex_e, vertex_f]

    graph.add_directed_edge(vertex_a, vertex_b, 1)
    graph.add_directed_edge(vertex_a, vertex_c, 2)
    graph.add_undirected_edge(vertex_b, vertex_c, 1)
    graph.add_undirected_edge(vertex_b, vertex_d, 3)
    graph.add_directed_edge(vertex_b, vertex_e, 2)
    graph.add_undirected_edge(vertex_c, vertex_e, 2)
    graph.add_directed_edge(vertex_d, vertex_c, 1)
    graph.add_undirected_edge(vertex_d, vertex_e, 4)
    graph.add_directed_edge(vertex_d, vertex_f, 3)
    graph.add_directed_edge(vertex_e, vertex_f, 3)

    paths_valid, info_map = graph.bellman_ford_shortest_path(vertex_a)

    if not paths_valid:
        print("A reachable negative-weight cycle exists.")
        return

    print_table(vertex_a, vertices, info_map)


if __name__ == "__main__":
    main()
