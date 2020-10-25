
from fastapi import FastAPI
from typing import List, Optional
from tsp_test_match.datamodels import Submission, SubmissionResponse, LeaderBoard, Cities
from tsp_test_match.tspmanager import TspManager



app = FastAPI()
tsp_manager = TspManager()

@app.get("/")
async def root():
    return "Hello There"

@app.get("/leaderboard", response_model=LeaderBoard)
async def leaderboard():
    game = tsp_manager.get_game()
    return game.get_leaderboard()

@app.get("/cities", response_model=Cities)
async def cities():
    game = tsp_manager.get_game()
    return game.get_cities()

@app.post("/submit",response_model=SubmissionResponse)
async def submit(submission: Submission):
    game = tsp_manager.get_game()
    return game.submit(submission)

