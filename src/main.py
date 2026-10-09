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


if __name__ == "__main__":
    main()