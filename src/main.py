from entities import Position
from simulator import Grid
from simulator.grid_queries import get_driveways, find_best_office
from automation import CityGenerator
from pathfinding import bfsPath

def connect_city(grid):
    house_driveways, office_driveways = get_driveways(grid) #get all driveways
    roads_built = 0

    for house in house_driveways:
        office, path = find_best_office(grid, house, office_driveways)

        if office is None:
            continue

        if path is None:
            print(f"No reachable office for {house}")
            continue

        # print(f"\nHouse driveway: {house}")
        # print(f"Chosen office driveway: {office}")
        # print(f"Path distance: {len(path) - 1}")

        for position in path[1:-1]:
            if grid.is_empty(position):
                if grid.add_road(position):
                    roads_built += 1

    return roads_built

def main() -> None:
    #Fixed Grid Generation
    # grid = Grid(10, 10, seed=42)
    # generator = CityGenerator(grid, seed=42)

    #Random Grid Genertion
    grid = Grid(10, 10)
    generator = CityGenerator(grid)
    
    houses_placed, offices_placed = generator.generate()

    print(f"Houses placed: {houses_placed}")
    print(f"Offices placed: {offices_placed}")

    print("\nGenerated city:")
    grid.print_grid()

    roads_built = connect_city(grid)

    print(f"\nNew road cells built: {roads_built}")
    print("\nCity after road construction:")
    grid.print_grid()


if __name__ == "__main__":
    main()