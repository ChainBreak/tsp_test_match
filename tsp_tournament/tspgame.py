
from tsp_tournament.datamodels import Submission, SubmissionResponse, LeaderBoard, Cities

class TspGame():

    def __init__(self):
        self.leader_board = []

    def submit(self, submission : Submission) ->  SubmissionResponse:
        return SubmissionResponse(rank = 69)

    def get_cities(self) -> Cities:
        return Cities(city_locations=[ [0,0], [0,1], [1,1], [1,0] ])


    def get_leaderboard(self) -> LeaderBoard:
        submission_list = [
            Submission(user_name="1",city_order=[1,2,3]),
            Submission(user_name="2",city_order=[3,2,1]),
        ]
        return LeaderBoard(submission_count=1, leading_submissions=submission_list)

