from config.config import DEAD, ALIVE, DEAD_COLOR, ALIVE_COLOR


class Cell():
    def __init__(self, state):
        self.state = state
        if self.state == ALIVE:
            self.color = ALIVE_COLOR
        elif self.state == DEAD:
            self.color = DEAD_COLOR
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def alive_neighbors(self):
        alive = 0
        for neighbor in self.neighbors:
            if neighbor.state == ALIVE:
                alive = alive + 1
        return alive

    def __str__(self):
        return 'state: {0}'.format(self.state)
