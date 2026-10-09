from entities import Position
from simulator import Grid
from automation import CityGenerator


def main() -> None:

    grid = Grid(12, 12)

    generator = CityGenerator(grid, seed=42)
    houses_placed, offices_placed = generator.generate()

    print(f"Houses placed: {houses_placed}")
    print(f"Offices placed: {offices_placed}")

    grid.print_grid()


################################
    from entities import House, Office, Position

    for row in range(grid.rows):
        for col in range(grid.cols):
            cell = grid.layout[row, col]
            position = Position(row, col)

            is_driveway = (
                isinstance(cell, House) and cell.position != position
            ) or (
                isinstance(cell, Office)
                and position not in cell.building_positions
            )

            if not is_driveway:
                continue

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < grid.rows and 0 <= nc < grid.cols):
                    continue

                neighbor = grid.layout[nr, nc]

                if isinstance(neighbor, (House, Office)) and neighbor is not cell:
                    print(f"Adjacent building/driveway at ({nr}, {nc})")

################################


if __name__ == "__main__":
    main()