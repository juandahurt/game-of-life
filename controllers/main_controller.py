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
        self.reload()
        root.mainloop()

    def reload(self):
        birth_rate = self.main_view.scl_birth_rate.get()
        print(birth_rate)
        self.cellular_automaton = CellularAutomaton(birth_rate, 10, 10)

    def update(self):
        if hasattr(self, 'main_view'):
            self.main_view.draw_ca()
            self.cellular_automaton.evolve()
