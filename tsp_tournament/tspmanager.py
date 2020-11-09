# The TSP Manager should be responsible for create a new game each day/week
import time
from datetime import datetime, timedelta
from tsp_tournament.tspgame import TspGame

class TspManager():
    def __init__(self):
        self.game = TspGame()
        self.end_datetime = self.compute_end_datetime()

    def compute_end_datetime(self):
        now = datetime.now()
        end_date = datetime(now.year,now.month,now.day, hour= 12)

        if now > end_date:
            end_date += timedelta(days = 1)

        return end_date

    def get_game(self):
                
        if datetime.now() > self.end_datetime:
            self.game = TspGame()
            self.end_datetime = self.compute_end_datetime()
        return self.game
