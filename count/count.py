from colorama import Fore

from ascii_games import Game, COLOURS


class Count(Game):
    FINAL_COUNT = 60

    def run(self):
        while True:
            self.model += 1
            self.render()
            if self.model == self.FINAL_COUNT:
                break

    @property
    def display(self):
        colour_index = self.model % len(COLOURS)
        colour = getattr(Fore, COLOURS[colour_index])
        return f"{colour}{self.model}"
