#!/usr/bin/python3

import json


class Base:
    """first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method returns the JSON string representation of
            list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    # @classmethod
    # def save_to_file(cls, list_objs):
    #     list_objs is None
    #
    #     l = list_objs
    #     f.write(json.dumps(l, sort_keys=True, indent=4))

    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of the JSON string
        representation"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.dumps(json_string)

    # @classmethod
    # def create(cls, **dictionary):
    # """Returns an instance with all attributes already set"""

