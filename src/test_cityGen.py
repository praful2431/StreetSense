
import unittest
import numpy as np

from simulator import Grid
from automation import CityGenerator


class TestCityGenerator(unittest.TestCase):

    def test_generate_places_entities(self):
        grid = Grid(20, 20, seed=42)
        generator = CityGenerator(grid, seed=42)

        houses, offices = generator.generate()

        self.assertGreater(houses + offices, 0)

    def test_generation_returns_nonnegative_counts(self):
        grid = Grid(20, 20, seed=42)
        generator = CityGenerator(grid, seed=42)

        houses, offices = generator.generate()

        self.assertGreaterEqual(houses, 0)
        self.assertGreaterEqual(offices, 0)

    def test_generated_entities_match_reported_counts(self):
        from entities import House, Office

        grid = Grid(20, 20, seed=42)
        generator = CityGenerator(grid, seed=42)

        houses_reported, offices_reported = generator.generate()

        houses_found = set()
        offices_found = set()

        for row in range(grid.rows):
            for col in range(grid.cols):
                cell = grid.layout[row, col]

                if isinstance(cell, House):
                    houses_found.add(cell)

                elif isinstance(cell, Office):
                    offices_found.add(cell)

        self.assertEqual(len(houses_found), houses_reported)
        self.assertEqual(len(offices_found), offices_reported)

    def test_small_grid_terminates(self):
        grid = Grid(1, 1, seed=42)
        generator = CityGenerator(grid, seed=42)

        houses, offices = generator.generate()

        self.assertGreaterEqual(houses, 0)
        self.assertGreaterEqual(offices, 0)

    def test_invalid_grid_dimensions(self):
        with self.assertRaises(ValueError):
            Grid(0, 10)


if __name__ == "__main__":
    unittest.main()