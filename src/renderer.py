from src.entities.house import House
from src.entities.office import Office
from src.entities.road import Road

-----------------------
def print_grid(grid):
    for row in grid.layout:
        for cell in row:
            if isinstance(cell, House):
                print("H ", end="")
            elif isinstance(cell, Office):
                print("O ", end="")
            elif isinstance(cell, Road):
                print("R ", end="")
            else:
                print(". ", end="")
        print()