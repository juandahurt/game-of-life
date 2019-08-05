from models.cellular_automaton import CellularAutomaton
from tkinter import Tk
from views.main_view import MainView


class MainController():
    """ This class it's in charge of the Main View behavior
    """
    def __init__(self):
        root = Tk()
        self.main_view = MainView(root, self)
        self.cellular_automaton = None
        self.rows = -1
        self.cols = -1
        self.reload()
        root.mainloop()

    def reload(self):
        # Get the birth rate
        birth_rate = self.main_view.scl_birth_rate.get()

        # Get CA dimensions
        self.rows = int(self.main_view.spx_rows.get())
        self.cols = int(self.main_view.spx_cols.get())

        self.cellular_automaton = CellularAutomaton(
            birth_rate,
            self.rows,
            self.cols
        )

        self.main_view.resize_cells(self.rows, self.cols)

    def update(self):
        # It's called every frame
        if hasattr(self, 'main_view'):
            self.main_view.draw_ca(self.cellular_automaton)
            self.cellular_automaton.evolve()
