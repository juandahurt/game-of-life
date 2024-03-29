from config.config import *
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
        self.canvas.grid(
            row=0,
            column=0,
            columnspan=3
        )

        self.lbl_birth_rate = Label(
            self.root,
            text='Birth rate'
        )
        self.lbl_birth_rate.grid(row=1, column=1)

        self.scl_birth_rate = Scale(
            self.root,
            from_=0,
            to=100,
            orient=HORIZONTAL
        )
        self.scl_birth_rate.grid(row=2, column=1)

        self.lbl_rows = Label(
            self.root,
            text='Rows'
        )
        self.lbl_rows.grid(row=1, column=0)

        self.spx_rows = Spinbox(
            root,
            from_=50,
            to=100,
            state='readonly'
        )
        self.spx_rows.grid(row=2, column=0, padx=20)

        self.lbl_cols = Label(
            self.root,
            text='Cols'
        )
        self.lbl_cols.grid(row=1, column=2)

        self.spx_cols = Spinbox(
            root,
            from_=50,
            to=100,
            state='readonly'
        )
        self.spx_cols.grid(row=2, column=2, padx=20)

        self.btn_reload = Button(
            self.root,
            text='Reload',
            command=self.controller.reload
        )
        self.btn_reload.grid(row=3, column=1)

        # Get the height and width
        window_width = root.winfo_reqwidth()
        window_height = root.winfo_reqheight()

        position_right = int(root.winfo_screenwidth() / 2 - WIDTH / 2)
        position_down = int(root.winfo_screenheight() / 2 - HEIGHT)

        # Position the window at the center of the screen
        root.geometry("+{}+{}".format(position_right, position_down))

        self.loop()

    def resize_cells(self, rows, cols):
        # Get the dimensions of every cell
        self.cell_width = WIDTH / cols
        self.cell_height = HEIGHT / rows

    def draw_ca(self, ca):
        # Clear the canvas
        self.canvas.delete('all')

        for row in range(ca.rows):
            for col in range(ca.cols):
                x = col * self.cell_width
                y = row * self.cell_height
                cell = ca.cells[row][col]
                self.canvas.create_rectangle(
                    x,
                    y,
                    x + self.cell_width,
                    y + self.cell_height,
                    fill=cell.color,
                    width=0.1,
                    outline=DEAD_COLOR
                )

    def loop(self):
        # The main loop
        self.controller.update()
        self.root.after(DELAY, self.loop)
