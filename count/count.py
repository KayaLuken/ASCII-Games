import time

from ascii_games import Game, COLOURS, bit


class Count(Game):
    FINAL_COUNT = 60

    def cycle(self):
        self.model += 1

    @property
    def is_terminated(self):
        if self.model == self.FINAL_COUNT:
            return True

    @property
    def display(self):
        colour_index = self.model % len(COLOURS)
        return [[bit(self.model, COLOURS[colour_index])]]
