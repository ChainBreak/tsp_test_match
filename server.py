
from fastapi import FastAPI
from typing import List, Optional
from datamodels import Submission, SubmissionResponse, LeaderBoard, Cities
from tspmanager import TspManager




app = FastAPI()
tsp_manager = TspManager()

@app.get("/")
async def root():
    return "Hello There"

@app.get("/leader_board", response_model=LeaderBoard)
async def leader_board():
    pass

@app.get("/cities", response_model=Cities)
async def cities():
    game = tsp_manager.get_game()
    return game.get_cities()

@app.post("/submit",response_model=SubmissionResponse)
async def submit(submission: Submission):
    game = tsp_manager.get_game()
    return game.submit(submission)

