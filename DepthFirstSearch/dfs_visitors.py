from abc import ABC, abstractmethod

from graph_components import Vertex


class VertexVisitor(ABC):
    """Abstract base class for objects that process visited vertices."""

    @abstractmethod
    def visit(self, vertex: Vertex) -> None:
        """Process a visited vertex."""


class PrintVertexVisitor(VertexVisitor):
    """Print each vertex encountered during traversal."""

    def visit(self, vertex: Vertex) -> None:
        """Print a visited vertex to the console."""
        print(vertex, end=" ")
