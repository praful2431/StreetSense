import unittest

from simulator import Grid
from automation import CityGenerator


class TestCityGenerator(unittest.TestCase):
    def test_generates_requested_entities_when_space_is_available(self):
        grid = Grid(20, 20)
        generator = CityGenerator(grid, seed=42)

        houses, offices = generator.generate()

        self.assertEqual(houses, 5)
        self.assertEqual(offices, 2)

    def test_returns_zero_for_zero_requested(self):
        grid = Grid(10, 10)
        generator = CityGenerator(grid, seed=42)

        self.assertEqual(generator.gen_houses(0), 0)
        self.assertEqual(generator.gen_offices(0), 0)

    def test_does_not_loop_forever_when_grid_is_full(self):
        grid = Grid(1, 1)
        generator = CityGenerator(grid, seed=42)

        placed = generator.gen_houses(10)

        self.assertLessEqual(placed, 1)

    def test_rejects_negative_count(self):
        grid = Grid(10, 10)
        generator = CityGenerator(grid, seed=42)

        with self.assertRaises(ValueError):
            generator.gen_houses(-1)


if __name__ == "__main__":
    unittest.main()