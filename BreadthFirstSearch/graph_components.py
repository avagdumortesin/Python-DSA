"""Graph component classes used by the breadth-first search implementation."""
from dataclasses import dataclass


@dataclass(eq=False, slots=True)
class Vertex:
    """Represents a vertex in a graph.

    Attributes:
        label: The unique label that identifies the vertex.
    """

    label: str


@dataclass(eq=False, slots=True)
class Edge:
    """Represents a weighted edge connecting two vertices.

    Attributes:
        from_vertex: The source vertex.
        to_vertex: The destination vertex.
        weight: The cost associated with traversing the edge.
    """

    from_vertex: Vertex
    to_vertex: Vertex
    weight: float
