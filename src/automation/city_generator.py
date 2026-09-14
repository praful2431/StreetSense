import random

from entities import Position
from simulator import Grid

class CityGenerator:
    def __init__(self, grid: Grid, seed: int | None = None):
        self.grid = grid
        self.random = random.Random(seed)

    #find a random position
    def _rand_position(self) -> Position:
        return Position(row = self.random.randrange(self.grid.rows), col = self.random.randrange(self.grid.cols))

    #general function to be used
    def generate(self) -> tuple[int, int]:
        houses_placed = 0
        offices_placed = 0
        choices = ["house", "office"]

        while ((2*houses_placed + 5*offices_placed) / (self.grid.rows * self.grid.cols) <= 0.2):

            entity_type = self.random.choice(choices)
            position = self._rand_position()

            if entity_type == "house":
                if self.grid.add_house(position) is not None:
                    houses_placed += 1
            else:
                if self.grid.add_office(position) is not None:
                    offices_placed += 1

        return houses_placed, offices_placed

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