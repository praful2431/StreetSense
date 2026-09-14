import random
import numpy as np
from entities import (Direction, House, Office, Position, Road, OFFICE_DRIVEWAY_OFFSETS)


class Grid:
    EMPTY = 0

    def __init__(self, rows: int, cols: int):
        if rows <= 0 or cols <= 0:
            raise ValueError("Grid dimensions must be positive.")

        self.rows = rows
        self.cols = cols
        self.layout = np.full((rows, cols), self.EMPTY, dtype=object)

    def is_valid_position(self, position: Position) -> bool:
        return 0 <= position.row < self.rows and 0 <= position.col < self.cols

    def is_empty(self, position: Position) -> bool:
        return self.is_valid_position(position) and self.layout[position.row, position.col] == self.EMPTY

    def _place(self, position: Position, item: object) -> bool:
        if not self.is_empty(position): return False

        self.layout[position.row, position.col] = item
        return True

    def add_road(self, position: Position) -> bool:
        return self._place(position, Road(position))

    def add_house(self, position: Position) -> House | None:
        if not self.is_empty(position):
            return None

        directions = list(Direction)
        random.shuffle(directions)

        for direction in directions:
            house = House(position, direction)

            if self.is_empty(house.driveway_position):
                self.layout[position.row, position.col] = house
                self.layout[house.driveway_position.row, house.driveway_position.col] = house
                return house

        return None

    def add_office(self, position: Position) -> Office | None:

        possible_anchors = [
            Position(position.row, position.col),
            Position(position.row, position.col - 1),
            Position(position.row - 1, position.col),
            Position(position.row - 1, position.col - 1),
        ]

        random.shuffle(possible_anchors)

        for anchor in possible_anchors:
            if not self.is_valid_position(anchor):
                continue

            for driveway_offset in random.sample(
                OFFICE_DRIVEWAY_OFFSETS,
                len(OFFICE_DRIVEWAY_OFFSETS),
            ):
                office = Office(anchor, driveway_offset)

                required_positions = (
                    office.building_positions
                    + (office.driveway_position,)
                )

                if all(
                    self.is_empty(pos)
                    for pos in required_positions
                ):
                    for pos in required_positions:
                        self.layout[pos.row, pos.col] = office

                    return office

        return None

    def remove_road(self, position: Position) -> bool:
        if not self.is_valid_position(position): return False

        item = self.layout[position.row, position.col]
        if not isinstance(item, Road):
            return False

        self.layout[position.row, position.col] = self.EMPTY
        return True

    def print_grid(self) -> None:
        symbols = {self.EMPTY: "."}

        for row in range(self.rows):
            cells = []

            for col in range(self.cols):
                item = self.layout[row, col]

                if item == self.EMPTY:
                    symbol = "."
                elif isinstance(item, Road):
                    symbol = "R"
                elif isinstance(item, House):
                    symbol = "H" if item.position == Position(row, col) else "d"
                elif isinstance(item, Office):
                    symbol = "O" if Position(row, col) in item.building_positions else "d"
                else:
                    symbol = "?"

                cells.append(symbol)

            print(" ".join(cells))