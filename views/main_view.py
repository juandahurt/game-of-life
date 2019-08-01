from config.config import WIDTH, HEIGHT
from tkinter import *


class MainView():
    """ Main View of the application.
    """
    def __init__(self, root, controller):
        self.root = root
        self.root.title('Game of Life!')
        self.controller = controller

        self.canvas = Canvas(
            self.root,
            bg='white',
            height=HEIGHT,
            width=WIDTH
        )
        self.canvas.pack()

        # Get the height and width
        window_width = root.winfo_reqwidth()
        window_height = root.winfo_reqheight()

        position_right = int(root.winfo_screenwidth() / 2 - WIDTH / 2)
        position_down = int(root.winfo_screenheight() / 2 - HEIGHT)

        # Position the window at the center of the screen
        root.geometry("+{}+{}".format(position_right, position_down))

    def loop():
        # main loop
        pass
