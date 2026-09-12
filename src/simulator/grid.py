import numpy as np
from numpy import random

class Grid:

    def __init__(self, row, col):
        self.layout = np.zeros((row, col))

#####      0 -> .       1 -> R       2 -> H       3 -> O

    def add_road(self, r, c):
        if(self.layout[r][c] != 0): return
        self.layout[r][c] = 1

    def add_house(self, r, c):
        if(self.layout[r][c] != 0): return
        self.layout[r][c] = 2

        #adding road to house
        directions = [(0, 1),   # Right
                      (0, -1),  # Left
                      (1, 0),   # Down
                      (-1, 0)]  # Up
        random.shuffle(directions)

        rows = len(self.layout)
        cols = len(self.layout[0])

        for dr, dc in directions:
            dwr = r + dr
            dwc = c + dc

            if (0 <= dwr < rows and 0 <= dwc < cols and self.layout[dwr][dwc] == 0):
                self.layout[dwr][dwc] = 1
                return

        self.layout[r][c] = 0


    def add_office(self, r, c):
        if(self.layout[r][c] != 0): return
        self.layout[r][c] = 3

    def remove_item(self, r, c):
        if(self.layout[r][c] == 1): self.layout[r][c] = 0

    def print_grid(self):
        for r in self.layout:
            for c in r:
                if(c == 0): print(". ", end="")
                elif(c == 1): print("R ", end="")
                elif(c == 2): print("H ", end="")
                elif(c == 3): print("O ", end="")
            print() #new line
        print("\n")
        

city = Grid(10, 10)
city.add_house(2, 3)
city.add_house(0, 0)
city.add_road(1, 1)
city.add_house(2, 1)
city.add_office(7, 3)
city.print_grid()