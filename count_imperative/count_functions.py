import sys
import time

import colorama
from colorama import Fore

from ascii_games import Game, COLOURS, bit
from math import inf

FINAL_COUNT = 60


def initialise_game(model, framerate=inf):
    colorama.init()
    refresh_rate = 1 / framerate
    return model, refresh_rate


def cycle_game(model):
    return model + 1


def is_terminated(model):
    return model == FINAL_COUNT


def display_game(model):
    colour_index = model % len(COLOURS)
    return [[bit(model, COLOURS[colour_index])]]


def clear_screen(model):
    for line in display_game(model):
        sys.stdout.write("\x1b[1A\x1b[2K")


def render_game(model, refresh_rate):
    clear_screen(model)

    for line in display_game(model):
        output = ''
        for _bit in line:
            colour = getattr(Fore, _bit.colour)
            output += f"{colour}{str(_bit.symbol)}"
        sys.stdout.write(output)
        sys.stdout.write('\n')


def run_game(model, refresh_rate):
    while True:
        model = cycle_game(model)
        time.sleep(refresh_rate)
        render_game(model, refresh_rate)
        if is_terminated(model):
            break
    return model
