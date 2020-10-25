# tsp_test_match
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
pip install fastapi uvicorn pytest requests
```

Install this package in the virtual environment in edit mode.
This makes it easy for modules to find each other.
```
pip install -e .
```

# Run
Run the server. Reload means the server will restart automatically when you make code changes
```
uvicorn tsp_test_match.server:app --reload
```

# Test
```
pytest
```


# TODO
- 

# Ideas
- Each day we should position cities so that it favour different types of algorithms. eg draw a circle that a gready search will be best at

