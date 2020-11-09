
import asyncio
import io
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
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


# Load the demo client into a string
with open("demo_client.py",'r') as f:
    demo_code = f.read()

# Convert the python code into markdown and then html
demo_code_lines = demo_code.splitlines(True)
demo_code_md = "\t"+"\t".join(demo_code_lines)
demo_code_html = markdown(f"\n\t::python\n{demo_code_md}\n", extensions=["codehilite"]) # https://coderbook.com/@marcus/how-to-render-markdown-syntax-as-html-using-python


@app.get("/",response_class=HTMLResponse)
async def index(request: Request):

    template_dict = {
        "request": request, 
        "code_html": demo_code_html.replace("http://127.0.0.1:8000/",str(request.base_url)), 
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


@app.get("/demo_client.py",response_class=StreamingResponse)
async def demo(request: Request):

    # Edit the code to replace the base url with the url the client has used to reach the server.
    # This should mean the code runs without any edits
    demo_code_url = demo_code.replace("http://127.0.0.1:8000/",str(request.base_url) )
    
    # Wrap the string in stream file object and return it as a file
    return StreamingResponse( io.StringIO(demo_code_url) ,media_type='application/octet-stream')

