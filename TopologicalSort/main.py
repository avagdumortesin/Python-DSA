"""Demonstrate topological sorting of directed graphs."""

from graph import Graph
from graph_components import Vertex


def display_sorted(vertices: list[Vertex], graph_num: int) -> None:
    """Display a graph's topological ordering."""
    print(f"Graph {graph_num}: {', '.join(str(vertex) for vertex in vertices)}")

    print()


def main() -> None:
    """Build two directed graphs and demonstrate topological sorting."""
    graph1 = Graph()
    vertex_a = graph1.add_vertex("A")
    vertex_b = graph1.add_vertex("B")
    vertex_c = graph1.add_vertex("C")
    vertex_d = graph1.add_vertex("D")
    vertex_e = graph1.add_vertex("E")
    vertex_f = graph1.add_vertex("F")
    vertex_g = graph1.add_vertex("G")
    graph1.add_directed_edge(vertex_a, vertex_b)
    graph1.add_directed_edge(vertex_a, vertex_c)
    graph1.add_directed_edge(vertex_b, vertex_f)
    graph1.add_directed_edge(vertex_c, vertex_d)
    graph1.add_directed_edge(vertex_d, vertex_f)
    graph1.add_directed_edge(vertex_e, vertex_f)
    graph1.add_directed_edge(vertex_e, vertex_g)
    graph1.add_directed_edge(vertex_f, vertex_g)

    graph2 = Graph()
    vertex_a = graph2.add_vertex("A")
    vertex_b = graph2.add_vertex("B")
    vertex_c = graph2.add_vertex("C")
    vertex_d = graph2.add_vertex("D")
    vertex_e = graph2.add_vertex("E")
    vertex_f = graph2.add_vertex("F")
    vertex_g = graph2.add_vertex("G")
    graph2.add_directed_edge(vertex_a, vertex_e)
    graph2.add_directed_edge(vertex_b, vertex_c)
    graph2.add_directed_edge(vertex_c, vertex_f)
    graph2.add_directed_edge(vertex_c, vertex_g)
    graph2.add_directed_edge(vertex_d, vertex_a)
    graph2.add_directed_edge(vertex_d, vertex_b)
    graph2.add_directed_edge(vertex_e, vertex_g)
    graph2.add_directed_edge(vertex_f, vertex_g)

    graphs = [graph1, graph2]

    for graph_num, graph in enumerate(graphs, start=1):
        sorted_vertices = graph.topological_sort()
        display_sorted(sorted_vertices, graph_num)


if __name__ == "__main__":
    main()
