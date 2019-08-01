from tkinter import Tk
from views.main_view import MainView


class MainController():
    def __init__(self):
        root = Tk()
        self.main_view = MainView(root, self)
        root.mainloop()
