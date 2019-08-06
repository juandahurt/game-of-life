from config.config import DEAD, ALIVE, BORN_COLOR, DYING_COLOR
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
        for row in range(self.rows):
            for col in range(self.cols):
                me = self.cells[row][col]
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        x = (row + i + self.rows) % self.rows
                        y = (col + j + self.cols) % self.cols
                        me.add_neighbor(self.cells[x][y])

    def evolve(self):
        new_gen = []
        for row in range(self.rows):
            new_row = []
            for col in range(self.cols):
                alive_neighbors = self.cells[row][col].alive_neighbors()
                me = self.cells[row][col]
                if me.state == ALIVE and alive_neighbors < 2:
                    cell = Cell(DEAD)
                    cell.color = DYING_COLOR
                    new_row.append(cell)
                elif me.state == ALIVE and (alive_neighbors == 2 or
                alive_neighbors == 3):
                    new_row.append(Cell(ALIVE))
                elif me.state == DEAD and alive_neighbors > 3:
                    new_row.append(Cell(DEAD))
                elif me.state == DEAD and alive_neighbors == 3:
                    cell = Cell(ALIVE)
                    cell.color = BORN_COLOR
                    new_row.append(cell)
                else:
                    new_row.append(Cell(me.state))
            new_gen.append(new_row)
        self.cells = new_gen
        self.set_neighbors()
