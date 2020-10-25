from pydantic import BaseModel
from typing import List, Optional

class Submission(BaseModel):
    user_name      : str
    algorithm_name : Optional[str]
    message        : Optional[str]
    city_order     : List[int]

class SubmissionResponse(BaseModel):
    rank : int

class Cities(BaseModel):
    city_locations : List[List[float]]

class LeaderBoard(BaseModel):
    submission_count     : int
    leading_submissions  : List[Submission]