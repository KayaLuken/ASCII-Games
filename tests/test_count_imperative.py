import pytest
from count import Count
from ascii_games import bit
from count_imperative.count_functions import initialise_game, cycle_game, display_game, run_game
from count_imperative.count_generators import count_generator


def test_count_functions_counts():
    model = 0
    model, refresh_rate = initialise_game(model)
    model = cycle_game(model)
    model = cycle_game(model)
    model = cycle_game(model)
    assert display_game(model) == [[bit(3, 'MAGENTA')]]
    model = run_game(model, refresh_rate)
    assert display_game(model) == [[bit(60, 'RED')]]


def test_count_generators_counts():
    model = 0
    count = count_generator(model)
    next(count)
    next(count)
    display = next(count)
    assert display == [[bit(3, 'MAGENTA')]]
    for i in count:
        display = i
    assert display == [[bit(60, 'RED')]]

