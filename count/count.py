import time

from ascii_games import Game, COLOURS, bit


class Count(Game):
    FINAL_COUNT = 60

    def cycle(self):
        self.model += 1

    def run(self):
        while True:
            self.cycle()
            time.sleep(self.refresh_rate)
            self.render()
            if self.model == self.FINAL_COUNT:
                break

    @property
    def display(self):
        colour_index = self.model % len(COLOURS)
        return [[bit(self.model, COLOURS[colour_index])]]
