#!/usr/bin/python3

import json

"""Function that creates an Object from a JSON file"""


def load_from_json_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
