from count_imperative.count_functions import initialise_game, cycle_game, display_game, run_game

if __name__ == '__main__':
    model = 0
    model, refresh_rate = initialise_game(0, framerate=3)
    model = run_game(model, refresh_rate)
