from __future__ import annotations

from dataclasses import dataclass
from math import inf

from GraphAlgorithms.shared.graph_components import Vertex


@dataclass(slots=True)
class PathVertexInfo:
    """Stores shortest-path information for a graph vertex."""

    vertex: Vertex
    distance: float = inf
    predecessor: Vertex | None = None
