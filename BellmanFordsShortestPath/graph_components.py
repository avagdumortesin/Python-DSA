"""Graph component classes used in weighted digraphs."""

from dataclasses import dataclass


@dataclass(eq=False, slots=True)
class Vertex:
    """Represents a vertex in a weighted digraph.

    Attributes:
        label: The label associated with the vertex.
    """

    label: str

    def __str__(self) -> str:
        return self.label


@dataclass(eq=False, slots=True)
class Edge:
    """Represents an edge in a weighted digraph.

    Attributes:
        from_vertex: The source vertex.
        to_vertex: The destination vertex.
        weight: The cost associated with traversing the edge.
    """

    from_vertex: Vertex
    to_vertex: Vertex
    weight: float
