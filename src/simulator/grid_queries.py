from entities import House, Office, Position
from simulator import Grid


def get_driveways(grid: Grid,) -> tuple[list[Position], list[Position]]:
    house_driveways = []
    office_driveways = []

    for row in range(grid.rows):
        for col in range(grid.cols):
            cell = grid.layout[row, col]
            position = Position(row, col)

            if isinstance(cell, House) and cell.position != position:
                house_driveways.append(position)

            elif (isinstance(cell, Office) and position not in cell.building_positions):
                office_driveways.append(position)

    return house_driveways, office_driveways