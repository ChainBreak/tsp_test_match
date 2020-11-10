import pytest
import numpy as np
from tsp_tournament.tspgame import TspGame


@pytest.mark.parametrize(
    "city_locations,path_length",
    [
        ([[0,0],[0, 1 ],[ 1 , 1 ] ,[1,0]], 4.0                       ),
        ([[0,0],[0, 1 ],[ 1 , 1 ]]       , 2+(2**0.5)                ),
        ([[0,0],[0,-10],[-10,-10]]       , 10+10+(10**2 + 10**2)**0.5),
        ([[0,0],[0,-10],[-10, 0 ]]       , 10+10+(10**2 + 10**2)**0.5),
    ],
)
def test_path_length(city_locations, path_length):
    tspgame = TspGame()
    tspgame.city_locations = city_locations
    tspgame.city_locations_np = np.array(city_locations)
    tspgame.num_cities = len(city_locations)
    
    city_order = list(range(len(city_locations)))
    assert pytest.approx(path_length) == tspgame.compute_path_length(city_order)

