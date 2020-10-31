
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
        self.leader_board = {}
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

            # Increase the submission count
            self.total_submission_count += 1

            # Update the leaderboard with this new entry
            self.update_leader_board(leaderboard_entry)

            # Respond saying its "all g mate"
            return SubmissionResponse(success=True , path_length=path_length, error_msg=""     )

        except Exception as e:
            return SubmissionResponse(success=False, path_length=-1.0       , error_msg=str(e) )

    def update_leader_board(self, leaderboard_entry):
        # Each user name can only be in the leaderboard once
        # User names are used to make unique entries

        # Get the user name for this entry
        user_name = leaderboard_entry.user_name

        # Check if the user is already in the leader board
        if user_name in self.leader_board:

            # Only update if the new entry is better
            # Check if the new entry is better than the current and update
            if leaderboard_entry.path_length < self.leader_board[user_name].path_length:
                self.leader_board[user_name] = leaderboard_entry

        else:
            #If not already in the list then just add it
            self.leader_board[user_name] = leaderboard_entry


    def get_cities(self) -> Cities:
        return Cities(city_locations=self.city_locations)


    def get_leaderboard(self) -> LeaderBoard:

        # Get the leader board entries
        leaderboard_list = self.leader_board.values()

        # Sort the leader board by the path lengths
        leaderboard_list = sorted(leaderboard_list, key=lambda x: x.path_length)

        # Return leaderboard
        return LeaderBoard(total_submission_count=self.total_submission_count, leading_submissions=leaderboard_list)


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
       
        


        