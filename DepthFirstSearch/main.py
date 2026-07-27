"""Demonstrate depth-first traversal across several graphs."""

from dfs_visitors import PrintVertexVisitor
from graph import Graph
from graph_components import Vertex


def create_graph(vertex_labels: list[str]) -> tuple[Graph, dict[str, Vertex]]:
    """Create a graph and return its vertices indexed by label."""
    graph = Graph()
    vertices = {label: graph.add_vertex(label) for label in vertex_labels}
    return graph, vertices


def main() -> None:
    start_vertex_label = "A"
    vertex_labels = ["A", "B", "C", "D", "E", "F"]

    graph_1, vertices_1 = create_graph(vertex_labels)
    graph_2, vertices_2 = create_graph(vertex_labels)
    graph_3, vertices_3 = create_graph(vertex_labels)

    graph_1.add_undirected_edge(vertices_1["A"], vertices_1["B"])
    graph_1.add_undirected_edge(vertices_1["A"], vertices_1["D"])
    graph_1.add_undirected_edge(vertices_1["B"], vertices_1["E"])
    graph_1.add_undirected_edge(vertices_1["B"], vertices_1["F"])
    graph_1.add_undirected_edge(vertices_1["C"], vertices_1["F"])
    graph_1.add_undirected_edge(vertices_1["E"], vertices_1["F"])

    graph_2.add_undirected_edge(vertices_2["A"], vertices_2["B"])
    graph_2.add_undirected_edge(vertices_2["B"], vertices_2["C"])
    graph_2.add_undirected_edge(vertices_2["C"], vertices_2["F"])
    graph_2.add_undirected_edge(vertices_2["D"], vertices_2["E"])
    graph_2.add_undirected_edge(vertices_2["E"], vertices_2["F"])

    graph_3.add_undirected_edge(vertices_3["A"], vertices_3["B"])
    graph_3.add_undirected_edge(vertices_3["A"], vertices_3["E"])
    graph_3.add_undirected_edge(vertices_3["B"], vertices_3["C"])
    graph_3.add_undirected_edge(vertices_3["B"], vertices_3["E"])
    graph_3.add_undirected_edge(vertices_3["C"], vertices_3["E"])
    graph_3.add_undirected_edge(vertices_3["D"], vertices_3["E"])
    graph_3.add_undirected_edge(vertices_3["E"], vertices_3["F"])

    graphs = [
        (graph_1, vertices_1),
        (graph_2, vertices_2),
        (graph_3, vertices_3),
    ]

    visitor = PrintVertexVisitor()

    print("Depth-first search traversal")
    for index, (graph, vertices) in enumerate(graphs, start=1):
        print(f"Graph {index}: ", end="")
        start_vertex = vertices.get(start_vertex_label)
        if start_vertex is None:
            print(f'Starting vertex "{start_vertex_label}" not found')
            continue

        graph.depth_first_search(start_vertex, visitor)
        print()


if __name__ == "__main__":
    main()
