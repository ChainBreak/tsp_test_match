
from datamodels import Submission, SubmissionResponse, LeaderBoard, Cities

class TspGame():

    def __init__(self):
        self.leader_board = []

    def submit(self, submission : Submission) ->  SubmissionResponse:
        return SubmissionResponse(rank = 69)

    def get_cities(self) -> Cities:
        #returns a square to test the city locations
        return Cities(city_locations=[ [0,0], [0,1], [1,1], [1,0] ])