import unittest
import numpy as np

from simulator import Grid
from automation.city_generator import CityGenerator


class TestCityGenerator(unittest.TestCase):

    def test_generate_takes_no_entity_counts(self):
        grid = Grid(20, 20)
        generator = CityGenerator(grid, seed=42)

        houses, offices = generator.generate()

        self.assertGreaterEqual(houses, 0)
        self.assertGreaterEqual(offices, 0)
        self.assertGreater(houses + offices, 0)

    def test_generation_is_reproducible_with_same_seed(self):
        grid1 = Grid(20, 20)
        grid2 = Grid(20, 20)

        generator1 = CityGenerator(grid1, seed=42)
        generator2 = CityGenerator(grid2, seed=42)

        result1 = generator1.generate()
        result2 = generator2.generate()

        self.assertEqual(result1, result2)
        np.testing.assert_array_equal(grid1.layout, grid2.layout)

    def test_generation_stays_near_twenty_percent_occupancy(self):
        grid = Grid(20, 20)
        generator = CityGenerator(grid, seed=42)

        generator.generate()

        occupied_cells = np.count_nonzero(grid.layout)
        total_cells = grid.rows * grid.cols
        occupancy = occupied_cells / total_cells

        # Allow some tolerance because buildings and driveways occupy
        # different numbers of cells.
        self.assertGreaterEqual(occupancy, 0.10)
        self.assertLessEqual(occupancy, 0.30)

    def test_small_grid_does_not_loop_forever(self):
        grid = Grid(1, 1)
        generator = CityGenerator(grid, seed=42)

        houses, offices = generator.generate()

        self.assertGreaterEqual(houses, 0)
        self.assertGreaterEqual(offices, 0)

    def test_negative_grid_dimensions_are_rejected(self):
        with self.assertRaises(ValueError):
            Grid(-1, 10)


if __name__ == "__main__":
    unittest.main()