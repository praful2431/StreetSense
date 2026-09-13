from dataclasses import dataclass
from .position import Position

@dataclass(frozen=True)
class Road:
    position: Position