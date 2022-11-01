import sys
import time
import colorama
from colorama import Fore, Style, Back

from math import inf



class Game:
    def __init__(self, model, frame_rate=inf):
        # need to do this to clear ANSI characters which are not recognised by windows
        colorama.init()
        self.frame_rate = frame_rate
        self.refresh_rate = 1 / self.frame_rate
        self.model = model

    def clear_screen(self):
        for line in self.display:
            sys.stdout.write("\x1b[1A\x1b[2K")

    def render(self):
        self.clear_screen()

        for line in self.display:
            output = ''
            for bit in line:
                colour = getattr(Fore, bit.colour)
                output += f"{colour}{str(bit.symbol)}"
            sys.stdout.write(output)
            sys.stdout.write('\n')

    def run(self):
        while True:
            self.cycle()
            time.sleep(self.refresh_rate)
            self.render()
            if self.is_terminated:
                break


