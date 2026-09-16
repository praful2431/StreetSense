from entities import Position
from simulator import Grid
from automation import CityGenerator


def main() -> None:
    grid = Grid(5, 5)

    grid.add_house(Position(0, 0))
    grid.add_road(Position(2,4))
    grid.add_office(Position(4, 4))
    grid.add_road(Position(4,2))

    grid.remove_road(Position(0,1))


    grid.print_grid()

    print("------------------------------------------------------------")
    grid = Grid(12, 12)

    generator = CityGenerator(grid, seed=42)
    houses_placed, offices_placed = generator.generate()

    print(f"Houses placed: {houses_placed}")
    print(f"Offices placed: {offices_placed}")

    grid.print_grid()


if __name__ == "__main__":
    main()