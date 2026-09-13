from dataclasses import dataclass
from .directions import Direction
from .position import Position

@dataclass(frozen=True)
class House:
    position: Position
    driveway_direction: Direction

    @property
    def driveway_position(self) -> Position:
        dr, dc = self.driveway_direction.offset

        return Position(
            self.position.row + dr,
            self.position.col + dc,
        )