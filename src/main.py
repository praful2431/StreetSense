from entities import Position
from simulator import Grid


def main() -> None:
    grid = Grid(rows=10, cols=10)

    grid.add_house(Position(2, 2))
    grid.add_office(Position(5, 4))
    grid.add_road(Position(0, 0))

    grid.print_grid()


if __name__ == "__main__":
    main()