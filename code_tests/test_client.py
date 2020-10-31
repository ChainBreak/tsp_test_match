import pytest
import uvicorn
import requests
import time

import numpy as np

from multiprocessing import Process

address = "127.0.0.1"
port = 1337

def run_server():
    uvicorn.run("tsp_tournament.server:app",host=address, port=port)

# https://docs.pytest.org/en/stable/fixture.html
@pytest.fixture(scope="session")
def server():
    proc = Process(target=run_server, args=(), daemon=True)
    proc.start() 
    time.sleep(0.5)
    yield
    proc.terminate() # Cleanup after test
    

def test_get_cities(server):
    response = requests.get(f"http://{address}:{port}/cities")
    assert response.status_code == 200
    assert type(response.json()["city_locations"]) is list
    assert np.array(response.json()["city_locations"]).ndim == 2

def test_get_leaderboard(server):
    response = requests.get(f"http://{address}:{port}/leaderboard")
    assert response.status_code == 200
    assert type(response.json()["total_submission_count"]) is int
    assert type(response.json()["leading_submissions"]) is list


def test_post_submit(server):
    data = {
        "user_name": "tom",
        "algorithm_name": "test_boy",
        "message": "hello",
        "city_order": [0,1,2,3]
    }
    response = requests.post(f"http://{address}:{port}/submit",json=data)
    assert response.status_code == 200



def test_dummy_player(server):
    response = requests.get(f"http://{address}:{port}/cities")
    assert response.status_code == 200
    city_locations = response.json()["city_locations"]

    data = {
        "user_name": "tom",
        "algorithm_name": "test_boy",
        "message": "hello",
        "city_order": list(range(len(city_locations)))
    }
    response = requests.post(f"http://{address}:{port}/submit",json=data)
    assert response.status_code == 200
    assert response.json()["path_length"] > 0.0

