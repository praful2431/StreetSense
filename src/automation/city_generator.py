import random

from entities import Position, House, Office
from simulator import Grid

class CityGenerator:
    def __init__(self, grid: Grid, seed: int | None = None):
        self.grid = grid
        self.random = random.Random(seed)

    #find a random position
    def _rand_position(self) -> Position:
        return Position(row = self.random.randrange(self.grid.rows), col = self.random.randrange(self.grid.cols),)

    #general function to be used
    def generate(self) -> tuple[int, int]:
        houses_placed = 0
        offices_placed = 0

        total_cells = self.grid.rows * self.grid.cols
        max_attempts = total_cells * 30
        attempts = 0

        self._ensure_minimum_buildings()

        while (
            (2 * houses_placed + 7 * offices_placed) / total_cells < 0.2
            and attempts < max_attempts
        ):
            attempts += 1
            entity_type = self.random.choice(["house", "office"])
            position = self._rand_position()

            if entity_type == "house":
                if self.grid.add_house(position) is not None:
                    houses_placed += 1
            else:
                if self.grid.add_office(position) is not None:
                    offices_placed += 1

        houses = set()
        offices = set()

        for row in self.grid.layout:
            for cell in row:
                if isinstance(cell, House):
                    houses.add(cell)
                elif isinstance(cell, Office):
                    offices.add(cell)

        return len(houses), len(offices)

    #input: grid & house count
    #output: return no. of houses placed
    def gen_houses(self, count: int) -> int:
        return self._generate(count, self.grid.add_house)

    #input: grid & office count
    #output: return no. of offices placed
    def gen_offices(self, count: int) -> int:
        return self._generate(count, self.grid.add_office)

    #helper function to place said entity
    def _generate(self, count: int, add_entity) -> int:
        if(count < 0): raise ValueError("count can't be negative")

        placed = 0
        max_attempts = count * 30

        while(placed != count and max_attempts != 0):
            position = self._rand_position()

            if(add_entity(position) is not None):
                placed += 1
            max_attempts -= 1

        return placed

    # helper function to ensure min. 1 house and 1 office
    def _ensure_minimum_buildings(self) -> None:
        if self.grid.rows * self.grid.cols < 2:
            raise ValueError(
                "Grid is too small to guarantee a house and an office."
            )

        has_house = any(
            isinstance(cell, House)
            for row in self.grid.layout
            for cell in row
        )

        if not has_house and self.gen_houses(1) != 1:
            raise ValueError("Could not place the minimum required house.")

        has_office = any(
            isinstance(cell, Office)
            for row in self.grid.layout
            for cell in row
        )

        if not has_office and self.gen_offices(1) != 1:
            raise ValueError("Could not place the minimum required office.")