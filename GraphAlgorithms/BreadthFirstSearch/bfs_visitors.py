from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from GraphAlgorithms.shared.graph_components import Vertex


class VertexVisitor(ABC):
    """Abstract base class for objects that process visited vertices."""

    @abstractmethod
    def visit(self, vertex: Vertex) -> None:
        """Process a visited vertex."""


@dataclass(slots=True)
class ListVertexVisitor(VertexVisitor):
    """Collects visited vertices in traversal order."""

    visited_vertices: list[Vertex] = field(default_factory=list)

    def visit(self, vertex: Vertex) -> None:
        """Add a visited vertex to the collection."""
        self.visited_vertices.append(vertex)
