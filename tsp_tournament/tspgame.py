
import math
import random
import numpy as np
from sortedcontainers import SortedList
from tsp_tournament.datamodels import Submission, SubmissionResponse, LeaderBoard,LeaderBoardEntry, Cities

# http://www.grantjenks.com/docs/sortedcontainers/sortedlist.html

class TspGame():

    def __init__(self):
        self.dim = 2
        self.max_leader_board_size = 5
        self.leader_board = []
        self.total_submission_count = 0
        self.city_locations = self.generate_city_locations()
        self.city_locations_np = np.array(self.city_locations)
        self.num_cities = len(self.city_locations)
        
 
        

    def submit(self, submission : Submission) ->  SubmissionResponse:
        try:
            # Calculate the lenght of the path for this submission
            # This will through some helpfull exceptions that will be sent back to the client through the json error message
            path_length = self.compute_path_length(submission.city_order)

            # Convert the submission to a leader board entry
            leaderboard_entry = LeaderBoardEntry(
                user_name      = submission.user_name,
                algorithm_name = submission.algorithm_name,
                message        = submission.message,
                city_order     = submission.city_order,
                path_length    = path_length,
            )

            self.total_submission_count += 1

            # Start off the rank as the current length of the leader board
            rank = len(self.leader_board)
            
            #start at the bottom of the leader to find the place to insert
            for i in range(len(self.leader_board)-1,-1,-1):
                # If the path is shorter than this spot in the leaderboard. set the rank to that spot
                # The rank is used as the index to insert this entry
                if path_length < self.leader_board[i].path_length:
                    rank = i
                else:
                    # If not smaller stop here
                    break

            # Insert this entry. Note that it will be append if rank is equal to the length
            self.leader_board.insert(rank,leaderboard_entry)

            # Remove the last entry if the leaderboard is full
            if len(self.leader_board) > self.max_leader_board_size:
                del self.leader_board[-1]

            # Set the rank to -1 if it is larger than our leaderboard
            if rank >= self.max_leader_board_size:
                rank = -1 


            return SubmissionResponse(rank = rank, path_length=path_length, error_msg="")

        except Exception as e:
            return SubmissionResponse(rank = -1, path_length=-1.0, error_msg=str(e))

       

    def get_cities(self) -> Cities:
        return Cities(city_locations=self.city_locations)


    def get_leaderboard(self) -> LeaderBoard:
        return LeaderBoard(total_submission_count=self.total_submission_count, leading_submissions=self.leader_board)


    def generate_city_locations(self):
        num_cities = random.randint(5,500)  
        return [[random.randint(50,1000) for d in range(self.dim)] for i in range(num_cities)]


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
       
        


        