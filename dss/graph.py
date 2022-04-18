from __future__ import annotations
from other.enum_helper import inc


class VerticeId(int):
    pass


class Vertice:
    _id: VerticeId
    name: str

    def __init__(self, name: str) -> None:
        self._id = inc("Vertice")
        self.name = name
    
    def __str__(self) -> str: return f"{self.name} [{self._id}]"

    def __repr__(self) -> str: return str(self)


class Edge:
    vertices: tuple[VerticeId, VerticeId]
    pass


class Graph:
    verices: dict[VerticeId, Vertice] = {}
    edges: dict[tuple[VerticeId, VerticeId], Edge] = {}
    # edges: set[Edge] = {}
