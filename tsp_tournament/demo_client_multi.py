import requests #pip install requests
import random

base_url = "http://127.0.0.1:8000/"

if __name__ == "__main__":

    # Request for all the cities.
    cities_response = requests.get(f"{base_url}cities")

    # Get the json data as python dict
    cities_json = cities_response.json()

    # Get the list of city locations from the dict
    city_locations = cities_json["city_locations"]

    # Print the number of cities that need to be visited
    print(f"Number of Cities:  {len(city_locations)}")

    # Print coordinates of the first city
    print(f"City 0 Location: {city_locations[0]}")

    # Create a defult list of every city index
    city_order = list(range(len(city_locations)))


    for i in range(15):
        ### WRITE YOUR SOLVER HERE ###
        random.shuffle(city_order)
        ##############################



        # Create a submission dict with the details of our submission
        submit_json = {
            "user_name"     : f"demo_client{i:02}",
            "algorithm_name": "random shuffle",
            "message"       : "Try and beat this fantastic algorithm",
            "city_order"    : city_order
        }

        # Post our submission to the server
        submission_response = requests.post(f"{base_url}submit",json=submit_json)

        # Get the json from the response to our submission
        submission_response_json = submission_response.json()

        # Print the details of our submission to see how we went
        print(f"Submit Success: {submission_response_json['success']}")
        print(f"Path Length   : {submission_response_json['path_length']}")




