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

    def init_cells(self):
        for _ in range(self.rows):
            row = []
            for _ in range(self.cols):
                rand = random() * 100
                cell = Cell(ALIVE) if rand <= self.birth_rate else Cell(DEAD)
                row.append(cell)
            self.cells.append(row)

    def evolve(self):
        print('evolve method not implemented!')
