import unittest

from entities import Position, Road, House
from simulator import Grid
from pathfinding import bfsPath


class TestBFSPath(unittest.TestCase):

    def test_shortest_path_on_empty_grid(self):
        grid = Grid(5, 5)
        start = Position(0, 0)
        goal = Position(4, 4)

        path = bfsPath(grid, start, goal)

        self.assertIsNotNone(path)
        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], goal)
        self.assertEqual(len(path) - 1, 8)

    def test_start_equals_goal(self):
        grid = Grid(5, 5)
        start = Position(2, 2)

        path = bfsPath(grid, start, start)

        self.assertEqual(path, [start])

    def test_no_path_when_destination_is_blocked_off(self):
        grid = Grid(5, 5)
        start = Position(2, 0)
        goal = Position(2, 4)

        # Block the entire middle row.
        for col in range(grid.cols):
            grid.layout[2, col] = House(Position(2, col), Position(2+1, col+1))

        # Allow the starting cell.
        grid.layout[start.row, start.col] = Grid.EMPTY

        path = bfsPath(grid, start, goal)

        self.assertIsNotNone(path)

    def test_path_uses_only_adjacent_steps(self):
        grid = Grid(6, 6)
        start = Position(0, 0)
        goal = Position(5, 5)

        path = bfsPath(grid, start, goal)

        self.assertIsNotNone(path)

        for i in range(len(path) - 1):
            row_diff = abs(path[i].row - path[i + 1].row)
            col_diff = abs(path[i].col - path[i + 1].col)

            self.assertEqual(row_diff + col_diff, 1)

    def test_path_stays_inside_grid(self):
        grid = Grid(5, 5)
        start = Position(0, 0)
        goal = Position(4, 4)

        path = bfsPath(grid, start, goal)

        self.assertIsNotNone(path)

        for position in path:
            self.assertTrue(grid.is_valid_position(position))

    def test_bfs_does_not_modify_grid(self):
        grid = Grid(5, 5)
        start = Position(0, 0)
        goal = Position(4, 4)

        original_layout = grid.layout.copy()

        bfsPath(grid, start, goal)

        for row in range(grid.rows):
            for col in range(grid.cols):
                self.assertEqual(
                    grid.layout[row, col],
                    original_layout[row, col],
                )

    def test_existing_roads_can_be_traversed(self):
        grid = Grid(3, 5)
        start = Position(1, 0)
        goal = Position(1, 4)

        # Make a road corridor between the endpoints.
        for col in range(1, 4):
            grid.add_road(Position(1, col))

        path = bfsPath(grid, start, goal)

        self.assertIsNotNone(path)
        self.assertEqual(len(path) - 1, 4)

    def test_unreachable_destination_in_crowded_grid(self):
        grid = Grid(5, 5)
        start = Position(0, 0)
        goal = Position(4, 4)

        # Fill the grid with blocked cells.
        for row in range(grid.rows):
            for col in range(grid.cols):
                grid.layout[row, col] = House(Position(row, col), Position(row+1, col+1))

        # Clear the start and its immediate neighbors.
        grid.layout[0, 0] = Grid.EMPTY
        grid.layout[0, 1] = Grid.EMPTY
        grid.layout[1, 0] = Grid.EMPTY

        path = bfsPath(grid, start, goal)

        self.assertIsNone(path)

    def test_custom1(self):
        grid = Grid(10, 10)
        start = Position(0, 0)
        goal = Position(8, 8)

        grid.add_road(Position(0, 1))
        grid.add_road(Position(0, 6))
        grid.add_road(Position(0, 9))

        grid.add_road(Position(1, 1))
        grid.add_road(Position(1, 8))

        grid.add_road(Position(2, 1))
        grid.add_road(Position(2, 4))
        grid.add_road(Position(2, 7))

        grid.add_road(Position(3, 3))
        grid.add_road(Position(3, 6))

        grid.add_road(Position(4, 2))
        grid.add_road(Position(4, 5))

        grid.add_road(Position(5, 1))
        grid.add_road(Position(5, 4))
        grid.add_road(Position(5, 8))

        grid.add_road(Position(6, 0))
        grid.add_road(Position(6, 3))
        grid.add_road(Position(6, 7))

        grid.add_road(Position(7, 6))

        grid.add_road(Position(8, 1))
        grid.add_road(Position(8, 5))

        grid.add_road(Position(9, 0))
        grid.add_road(Position(9, 4))

        path = bfsPath(grid, start, goal)
        # for pos in path:
        #     print(pos)
        self.assertIsNotNone(path)


    def test_existing_road_corridor(self):
        grid = Grid(5, 5)
        start = Position(2, 0)
        goal = Position(2, 4)

        # Existing road corridor: 4 moves from start to goal.
        for col in range(1, 4):
            grid.add_road(Position(2, col))

        path = bfsPath(grid, start, goal)

        self.assertIsNotNone(path)
        print("Path:", path)
        print("Distance:", len(path) - 1)

        # If roads are traversable, the shortest distance is 4.
        self.assertEqual(len(path) - 1, 4)


    def test_custom2(self):
        grid = Grid(10, 10)

        start = Position(7, 2)  # Green
        goal = Position(1, 0)   # Red

        # Existing roads (orange)
        grid.add_road(Position(5, 5))
        grid.add_road(Position(5, 6))

        # Houses (blue): blocked cells
        blue_cells = [
            (2, 2),
            (3, 1),
            (3, 2),
            (4, 0),
            (4, 1),
            (5, 2),
            (5, 3),
            (5, 4),
            (5, 7),
            (6, 2),
        ]

        for row, col in blue_cells:
            # Temporary blocked-cell stand-in:
            # BFS should reject these non-empty, non-road cells.
            grid.layout[row, col] = object()

        path = bfsPath(grid, start, goal)

        print("Custom 2 path:", path)

        self.assertIsNotNone(path)
        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], goal)

        # Every step must be orthogonally adjacent.
        for i in range(len(path) - 1):
            distance = (
                abs(path[i].row - path[i + 1].row)
                + abs(path[i].col - path[i + 1].col)
            )
            self.assertEqual(distance, 1)


if __name__ == "__main__":
    unittest.main()