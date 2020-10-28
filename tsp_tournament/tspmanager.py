# The TSP Manager should be responsible for create a new game each day/week
from tsp_tournament.tspgame import TspGame

class TspManager():
    def __init__(self):
        self.game = TspGame()

    def get_game(self):
        # TODO: Games need to be genereated each day
        return self.game
