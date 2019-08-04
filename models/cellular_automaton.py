from config.config import DEAD, ALIVE
from .cell import Cell
from random import random


class CellularAutomaton():
    def __init__(self, birth_rate, rows, cols):
        self.cells = []
        self.birth_rate = birth_rate
        self.rows = rows
        self.cols = cols
        self.init_cells()
        self.set_neighbors()

    def init_cells(self):
        for _ in range(self.rows):
            row = []
            for _ in range(self.cols):
                rand = random() * 100
                cell = Cell(ALIVE) if rand <= self.birth_rate else Cell(DEAD)
                row.append(cell)
            self.cells.append(row)

    def set_neighbors(self):
        # Von Neuman neighborhood
        for row in range(self.rows):
            for col in range(self.cols):
                me = self.cells[row][col]

                # Up
                if row == 0:
                    up = self.cells[self.rows - 1][col]
                else:
                    up = self.cells[row - 1][col]
                me.add_neighbor(up)

                # Right
                if col == self.cols - 1:
                    right = self.cells[row][0]
                else:
                    right = self.cells[row][col + 1]
                me.add_neighbor(right)

                # Down
                if row == self.rows - 1:
                    down = self.cells[0][col]
                else:
                    down = self.cells[row + 1][col]
                me.add_neighbor(down)

                # Left
                if col == 0:
                    left = self.cells[row][self.cols - 1]
                else:
                    left = self.cells[row][col - 1]
                me.add_neighbor(left)

    def evolve(self):
        new_gen = []
        for row in range(self.rows):
            new_row = []
            for col in range(self.cols):
                alive_neighbors = self.cells[row][col].alive_neighbors()
                if alive_neighbors == 2 or alive_neighbors == 3:
                    new_row.append(Cell(ALIVE))
                else:
                    new_row.append(Cell(DEAD))
            new_gen.append(new_row)
        self.cells.clear()
        self.cells = new_gen
        self.set_neighbors()
