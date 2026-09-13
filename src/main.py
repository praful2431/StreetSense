from entities import Position
from simulator import Grid


def main() -> None:
    grid = Grid(rows=10, cols=10)

    grid.add_house(Position(0, 0))
    grid.add_road(Position(4,5))
    grid.add_office(Position(5, 5))
    grid.add_road(Position(4,2))

    grid.remove_road(Position(0,1))


    grid.print_grid()


if __name__ == "__main__":
    main()