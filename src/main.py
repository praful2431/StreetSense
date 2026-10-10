from entities import Position, House, Office
from simulator import Grid
from automation import CityGenerator, bfs_path


def get_driveways(grid: Grid) -> tuple[list[Position], list[Position]]:
    house_driveways = []
    office_driveways = []

    for row in range(grid.rows):
        for col in range(grid.cols):
            cell = grid.layout[row, col]
            position = Position(row, col)

            if isinstance(cell, House) and cell.position != position:
                house_driveways.append(position)

            elif (
                isinstance(cell, Office)
                and position not in cell.building_positions
            ):
                office_driveways.append(position)

    return house_driveways, office_driveways


def main() -> None:
    grid = Grid(10, 10)
    generator = CityGenerator(grid, seed=42)

    houses_placed, offices_placed = generator.generate()

    print(f"Houses placed: {houses_placed}")
    print(f"Offices placed: {offices_placed}")
    grid.print_grid()


    house_driveways, office_driveways = get_driveways(grid)

    if not house_driveways or not office_driveways:
        print("Cannot run BFS: no house or office driveway found.")
        return


    start = house_driveways[0]
    goal = office_driveways[0]

    path = bfs_path.bfsPath(grid, start, goal)

    if path is None:
        print("No path found.")
        return

    print("\nPath found:")
    print(path)
    print(f"Path distance: {len(path) - 1}")


    for position in path[1:-1]:
        if grid.is_empty(position):
            grid.add_road(position)

    print("\nCity after road construction:")
    grid.print_grid()


if __name__ == "__main__":
    main()