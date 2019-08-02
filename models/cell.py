from config.config import DEAD, ALIVE


class Cell():
    def __init__(self, state):
        self.state = state
        self.neighbors = []

    def __str__(self):
        return 'state: {0}'.format(self.state)
