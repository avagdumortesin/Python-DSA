"""Demonstrate the Floyd-Warshall all-pairs shortest-path algorithm."""

from graph import Graph
from shortest_path_matrix import ShortestPathMatrix

from GraphAlgorithms.shared.graph_components import Vertex


def print_path_sequence(
    graph: Graph,
    start_vertex: Vertex,
    end_vertex: Vertex,
    matrix: ShortestPathMatrix,
) -> None:
    """Display the shortest path between two vertices."""
    print(f"Shortest path from {start_vertex.label} to {end_vertex.label}:")

    path = graph.reconstruct_path(
        start_vertex,
        end_vertex,
        matrix,
    )

    if not path:
        print("No path exists.")
    else:
        path_labels = [
            start_vertex.label,
            *(edge.to_vertex.label for edge in path),
        ]
        print(" to ".join(path_labels))

        print()

    print()


def main() -> None:
    """Build four weighted graphs and demonstrate the Floyd-Warshall algorithm."""
    graph_vertices = [
        ["A", "B", "C", "D"],
        ["A", "B", "C", "D"],
        ["A", "B", "C"],
        ["A", "B", "C", "D", "E"],
    ]

    graph_edges = [
        ["AB2", "BC-3", "BD7", "CA5", "DA-4"],
        ["AB4", "BC3", "CD6", "DA-1", "DB7"],
        ["AB1", "AC1", "BC-8"],
        ["AB1", "AE8", "BC2", "CD3", "DA-5", "ED9"],
    ]

    graph_paths = ["CD", "DB", "CA", "AD"]

    graph_data = zip(graph_vertices, graph_edges, graph_paths)

    for graph_num, (
        vertex_labels,
        edge_strings,
        path_string,
    ) in enumerate(graph_data, start=1):
        graph = Graph()

        vertices: dict[str, Vertex] = {
            label: graph.add_vertex(label) for label in vertex_labels
        }

        for edge_string in edge_strings:
            from_vertex = vertices[edge_string[0]]
            to_vertex = vertices[edge_string[1]]
            weight = float(edge_string[2:])

            graph.add_directed_edge(from_vertex, to_vertex, weight)

        matrix: ShortestPathMatrix = graph.all_pairs_shortest_path()

        print(f"All pairs shortest path matrix (graph {graph_num}):")
        matrix.print_matrix()

        start_vertex = vertices[path_string[0]]
        end_vertex = vertices[path_string[1]]

        print_path_sequence(graph, start_vertex, end_vertex, matrix)


if __name__ == "__main__":
    main()
