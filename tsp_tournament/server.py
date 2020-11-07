
import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Optional
from markdown import markdown
from tsp_tournament.datamodels import Submission, SubmissionResponse, LeaderBoard, Cities
from tsp_tournament.tspmanager import TspManager



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

tsp_manager = TspManager()

# https://coderbook.com/@marcus/how-to-render-markdown-syntax-as-html-using-python
with open("demo_client.py",'r') as f:
    code_lines = f.readlines()
    code = "\t"+"\t".join(code_lines)
    code_html = markdown(f"\n\t::python\n{code}\n", extensions=["codehilite"])


@app.get("/",response_class=HTMLResponse)
async def index(request: Request):

    template_dict = {
        "request": request, 
        "code_html": code_html.replace("http://127.0.0.1:8000/",str(request.base_url)), 
        "docs_url": f"{request.base_url}docs"
    }
    return templates.TemplateResponse("index.html", template_dict)

@app.get("/viewer",response_class=HTMLResponse)
async def viewer(request: Request):
    return templates.TemplateResponse("viewer.html", {"request": request,})

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

