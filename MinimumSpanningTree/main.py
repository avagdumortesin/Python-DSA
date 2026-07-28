"""Demonstrate minimum spanning tree constructions."""

from graph import Graph
from graph_components import Edge, Vertex


def display_tree(tree_edges: list[Edge], graph_num: int) -> None:
    """Display the edges in a minimum spanning tree."""
    print(f"Edges in minimum spanning tree (graph {graph_num}):")

    for edge in tree_edges:
        print(
            f"  {edge.from_vertex.label} -- "
            f"{edge.to_vertex.label}, "
            f"weight = {edge.weight:g}"
        )

    print()


def main() -> None:
    """Build two weighted graphs and demonstrate minimum spanning trees."""
    graph_1 = Graph()
    vertices_1: dict[str, Vertex] = {
        label: graph_1.add_vertex(label)
        for label in ["A", "B", "C", "D", "E", "F", "G", "H"]
    }
    graph_1.add_undirected_edge(vertices_1["A"], vertices_1["B"], 15)
    graph_1.add_undirected_edge(vertices_1["A"], vertices_1["D"], 6)
    graph_1.add_undirected_edge(vertices_1["B"], vertices_1["C"], 9)
    graph_1.add_undirected_edge(vertices_1["B"], vertices_1["D"], 12)
    graph_1.add_undirected_edge(vertices_1["B"], vertices_1["G"], 14)
    graph_1.add_undirected_edge(vertices_1["B"], vertices_1["H"], 10)
    graph_1.add_undirected_edge(vertices_1["C"], vertices_1["E"], 16)
    graph_1.add_undirected_edge(vertices_1["D"], vertices_1["E"], 8)
    graph_1.add_undirected_edge(vertices_1["E"], vertices_1["F"], 20)

    graph_2 = Graph()
    vertices_2: dict[str, Vertex] = {
        label: graph_2.add_vertex(label)
        for label in ["A", "B", "C", "D", "E", "F", "G", "P"]
    }
    graph_2.add_undirected_edge(vertices_2["A"], vertices_2["B"], 80)
    graph_2.add_undirected_edge(vertices_2["A"], vertices_2["C"], 105)
    graph_2.add_undirected_edge(vertices_2["A"], vertices_2["E"], 182)
    graph_2.add_undirected_edge(vertices_2["B"], vertices_2["C"], 90)
    graph_2.add_undirected_edge(vertices_2["B"], vertices_2["D"], 60)
    graph_2.add_undirected_edge(vertices_2["B"], vertices_2["P"], 100)
    graph_2.add_undirected_edge(vertices_2["C"], vertices_2["P"], 132)
    graph_2.add_undirected_edge(vertices_2["D"], vertices_2["E"], 80)
    graph_2.add_undirected_edge(vertices_2["E"], vertices_2["F"], 70)
    graph_2.add_undirected_edge(vertices_2["F"], vertices_2["G"], 72)
    graph_2.add_undirected_edge(vertices_2["F"], vertices_2["P"], 145)
    graph_2.add_undirected_edge(vertices_2["G"], vertices_2["P"], 180)

    graphs: list[Graph] = [graph_1, graph_2]

    for graph_num, graph in enumerate(graphs, start=1):
        tree_edges: list[Edge] = graph.minimum_spanning_tree()
        display_tree(tree_edges, graph_num)


if __name__ == "__main__":
    main()
