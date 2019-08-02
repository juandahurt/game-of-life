from config.config import WIDTH, HEIGHT, DELAY
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

        self.lbl_birth_rate = Label(
            self.root,
            text='Birth rate'
        )
        self.lbl_birth_rate.pack()

        self.scl_birth_rate = Scale(
            self.root,
            from_=0,
            to=100,
            orient=HORIZONTAL
        )
        self.scl_birth_rate.pack()

        self.btn_reload = Button(
            self.root,
            text='Reload',
            command=self.controller.reload
        )
        self.btn_reload.pack()

        # Get the height and width
        window_width = root.winfo_reqwidth()
        window_height = root.winfo_reqheight()

        position_right = int(root.winfo_screenwidth() / 2 - WIDTH / 2)
        position_down = int(root.winfo_screenheight() / 2 - HEIGHT)

        # Position the window at the center of the screen
        root.geometry("+{}+{}".format(position_right, position_down))

        self.loop()

    def loop(self):
        # main loop
        self.controller.update()
        self.root.after(DELAY, self.loop)

    def draw_ca(self):
        pass
