#!/usr/bin/python3

"""Python script that takes in a string and sends a search request to the
Star Wars API

Use the Star Wars API search people endpoint
Use the string argument as the search value of the request
The body response must be JSON and converted to a Python dictionary."""

import requests
from sys import argv

if __name__ == "__main__":

    s = {'search': argv[1]}
    res = requests.get("https://swapi.co/api/people", params=s)
    name_res = res.json()
    print("Number of results: {}".format(name_res.get("count")))
    for people in name_res.get("results"):
        print(people.get("name"))
