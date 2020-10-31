# The TSP Manager should be responsible for create a new game each day/week
import time
from tsp_tournament.tspgame import TspGame

class TspManager():
    def __init__(self):
        self.game = TspGame()
        self.start_time = time.time()

    def get_game(self):
        # TODO: Games need to be genereated each day

        current_time = time.time()
        if current_time - self.start_time > 60:
            self.game = TspGame()
            self.start_time = current_time

        return self.game
