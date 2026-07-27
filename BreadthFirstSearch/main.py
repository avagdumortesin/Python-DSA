"""Demonstrates breadth-first traversal of a graph."""

from bfs_visitors import ListVertexVisitor
from graph import Graph
from graph_components import Vertex


def main() -> None:
    """Create a graph and perform a breadth-first traversal."""
    start_name = "Eva"

    people_graph = Graph()

    vertex_a = people_graph.add_vertex("Joe")
    vertex_b = people_graph.add_vertex("Eva")
    vertex_c = people_graph.add_vertex("Taj")
    vertex_d = people_graph.add_vertex("Chen")
    vertex_e = people_graph.add_vertex("Lily")
    vertex_f = people_graph.add_vertex("Jun")
    vertex_g = people_graph.add_vertex("Ken")

    people_graph.add_undirected_edge(vertex_a, vertex_b)
    people_graph.add_undirected_edge(vertex_a, vertex_c)
    people_graph.add_undirected_edge(vertex_b, vertex_e)
    people_graph.add_undirected_edge(vertex_c, vertex_d)
    people_graph.add_undirected_edge(vertex_c, vertex_e)
    people_graph.add_undirected_edge(vertex_d, vertex_f)
    people_graph.add_undirected_edge(vertex_e, vertex_f)
    people_graph.add_undirected_edge(vertex_f, vertex_g)

    start_vertex = people_graph.get_vertex(start_name)
    visitor = ListVertexVisitor()

    if start_vertex is None:
        print(f'Start vertex "{start_name}" not found')
        return

    vertex_distances: dict[Vertex, int] = {}
    people_graph.breadth_first_search(start_vertex, visitor, vertex_distances)

    print("Breadth-first search traversal")
    print(f"Start vertex: {start_vertex.label}")

    for vertex in visitor.visited_vertices:
        print(f"{vertex.label}: {vertex_distances[vertex]}")


if __name__ == "__main__":
    main()
