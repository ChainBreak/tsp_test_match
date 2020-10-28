
import math
import random
import numpy as np
from sortedcontainers import SortedList
from tsp_tournament.datamodels import Submission, SubmissionResponse, LeaderBoard,LeaderBoardSubmission, Cities

# http://www.grantjenks.com/docs/sortedcontainers/sortedlist.html

class TspGame():

    def __init__(self):
        self.dim = 2
        self.leader_board = SortedList(key=lambda x: x.path_length)
        self.city_locations = self.generate_city_locations()
        self.city_locations_np = np.array(self.city_locations)
        self.num_cities = len(self.city_locations)
        
 
        

    def submit(self, submission : Submission) ->  SubmissionResponse:
        try:
            path_length = self.compute_path_length(submission.city_order)



            return SubmissionResponse(rank = -1, path_length=path_length, error_msg="")
        except Exception as e:
            return SubmissionResponse(rank = -1, path_length=-1.0, error_msg=str(e))

       

    def get_cities(self) -> Cities:
        return Cities(city_locations=self.city_locations)


    def get_leaderboard(self) -> LeaderBoard:
        submission_list = [
            LeaderBoardSubmission(user_name="1",city_order=[1,2,3]),
            LeaderBoardSubmission(user_name="2",city_order=[3,2,1]),
        ]
        return LeaderBoard(total_submission_count=1, leading_submissions=submission_list)


    def generate_city_locations(self):
        num_cities = random.randint(5,50)  
        return [[random.randint(0,10) for d in range(self.dim)] for i in range(num_cities)]


    def compute_path_length(self,city_order_list):
        
        #Convert this city index list into an array
        city_order = np.array(city_order_list)

        #make sure the smallest index is in range
        if city_order.min() < 0:
            raise Exception(f"City {city_order.min()} does not exist. The min city index is 0")
        
        #make sure the largest index is in range
        if city_order.max() >= self.num_cities:
            raise Exception(f"City {city_order.max()} does not exist. The max city index is {self.num_cities-1}")

        #create a check list to ensure every city is visited
        city_checklist = np.zeros(self.num_cities)
        
        #put a 1 in the check list for every city visited
        city_checklist[city_order] = 1
        
        #ensure that the checklist sums to the number of cities
        if city_checklist.sum() != self.num_cities:
            missing_city = int(np.where(city_checklist==0)[0][0])
            raise Exception(f"Did not visit city {missing_city}")

        #order the city locations by the city order
        ordered_city_locations = self.city_locations_np[city_order]

        # Subtract the current city positions from the next city positions in the path
        diff = ordered_city_locations - np.roll(ordered_city_locations,1,axis=0)

        # Calculate the distance between cities and sum this to get the whole path length
        path_length = np.sqrt((diff*diff).sum(axis=1)).sum()

        return path_length
       
        


        