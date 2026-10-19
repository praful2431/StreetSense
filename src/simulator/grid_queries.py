from entities import House, Office, Position
from simulator import Grid
from pathfinding import bfsPath

#input: Grid
#otuput: tupele(houseDriveways, officeDriveways)
def get_driveways(grid: Grid,) -> tuple[list[Position], list[Position]]:
    house_driveways = []
    office_driveways = []

    for row in range(grid.rows):
        for col in range(grid.cols):
            cell = grid.layout[row, col]
            position = Position(row, col)

            #check if the position is driveway and isn't the house itself
            if isinstance(cell, House) and cell.position != position:
                house_driveways.append(position)

            #check if the position is driveway and isn't the office itself
            elif (isinstance(cell, Office) and position not in cell.building_positions):
                office_driveways.append(position)

    return house_driveways, office_driveways

#input: Grid, House, and all Offices
#output: optimal office and path
def find_best_office(grid, house, offices):
    best_office = None
    best_path = None

    for office in offices:
        path = bfsPath(grid, house, office)

        if path is None:
            continue

        if best_path is None or len(path) < len(best_path):
            best_office = office
            best_path = path

    return best_office, best_path