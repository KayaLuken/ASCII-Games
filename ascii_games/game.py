import sys
import time

COLOURS = ['BLUE', 'CYAN', 'GREEN', 'MAGENTA', 'RED', 'WHITE', 'YELLOW']


class Game:
    def __init__(self, model, frame_rate=5):
        self.frame_rate = frame_rate
        self.refresh_rate = 1 / self.frame_rate
        self.model = model

    def render(self):
        sys.stdout.write(self.display)
        time.sleep(self.refresh_rate)
        sys.stdout.write('\r')
