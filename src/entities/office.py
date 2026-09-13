from dataclasses import dataclass
from .position import Position

OFFICE_DRIVEWAY_OFFSETS = (
    (-1, 0),  # above, left column
    (-1, 1),  # above, right column
    (0, -1),  # left, top row
    (1, -1),  # left, bottom row
    (0, 2),   # right, top row
    (1, 2),   # right, bottom row
    (2, 0),   # below, left column
    (2, 1),   # below, right column
)

@dataclass(frozen=True)
class Office:
    position: Position
    driveway_offset: tuple[int, int]

    def __post_init__(self) -> None:
        if self.driveway_offset not in OFFICE_DRIVEWAY_OFFSETS:
            raise ValueError("Invalid office driveway position.")

    @property
    def building_positions(self) -> tuple[Position, ...]:
        row, col = self.position.row, self.position.col

        return (
            Position(row, col),
            Position(row, col + 1),
            Position(row + 1, col),
            Position(row + 1, col + 1),
        )

    @property
    def driveway_position(self) -> Position:
        dr, dc = self.driveway_offset

        return Position(
            self.position.row + dr,
            self.position.col + dc,
        )