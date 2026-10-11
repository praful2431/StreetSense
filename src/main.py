
from entities import Position
from simulator import Grid
from simulator.grid_queries import get_driveways
from automation import CityGenerator
from pathfinding import bfsPath


def main() -> None:
    #Fixed Grid Generation
#    grid = Grid(10, 10, seed=42)

    #Random Grid Genertion
    grid = Grid(10, 10)

    generator = CityGenerator(grid, seed=42)

    houses_placed, offices_placed = generator.generate()

    print(f"Houses placed: {houses_placed}")
    print(f"Offices placed: {offices_placed}")

    print("\nGenerated city:")
    grid.print_grid()


    #house and office driveways
    house_driveways, office_driveways = get_driveways(grid)

    if not house_driveways or not office_driveways:
        print("\nCannot run BFS: no house or office driveway found.")
        return


    #house-office pair
    start = house_driveways[0]
    goal = office_driveways[0]

    print(f"\nStart driveway: {start}")
    print(f"Goal driveway:  {goal}")

    #shortest path
    path = bfsPath(grid, start, goal)

    if path is None:
        print("\nNo path found.")
        return

    print(f"\nPath distance: {len(path) - 1}")
    print("Path:")
    print(path)

    #roads
    roads_built = 0

    for position in path[1:-1]:
        if grid.is_empty(position):
            if grid.add_road(position):
                roads_built += 1

    print(f"\nNew road cells built: {roads_built}")
    print("\nCity after road construction:")
    grid.print_grid()


if __name__ == "__main__":
    main()