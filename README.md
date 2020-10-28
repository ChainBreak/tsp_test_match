# Traveling Salesman Problem Tournament
A Server that host a Traveling Salesman Problem Tournament where clients compete by submitting shortest paths

# Setup
 
Clone this repo
```
git clone git@github.com:ChainBreak/tsp_test_match.git
```

Navigate to this folder
```
cd path/to/tsp_test_match
```

Make sure you have you have virtual env installed
 ```
sudo apt install python3-venv
 ```

Create virtual environment
```
python3 -m venv env
```

Activate the virtual environment
```
source ./env/bin/activate
```

Install the required packages
```
pip install fastapi uvicorn pytest requests numpy
```

Install this package in the virtual environment in edit mode.
This makes it easy for modules to find each other.
```
pip install -e .
```

# Run
Run the server. Reload means the server will restart automatically when you make code changes
```
uvicorn tsp_tournament.server:app --reload
```

# Test
Just run pytest and it will find all the tests and run them
```
pytest code_tests
```

# Auto Docs
FastAPI is magic. It generates documentation based on the interface specified in the server.
When the server is running go to.
http://127.0.0.1:8000/docs


# TODO
- Implement tspgame so that it generates city locations.
- Make it so tspgame can rank paths in shortest order
- Make a client that renders the game for display on the big screen
- Make the tsp manager create a new game each day

# Ideas
- Each day we should position cities so that it favour different types of algorithms. eg draw a circle that a gready search will be best at.
- Make the number of cities big and small. Some days an exact solutions is possible and other days heuristics are needed.

