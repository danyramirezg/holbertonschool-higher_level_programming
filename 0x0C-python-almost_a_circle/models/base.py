#!/usr/bin/python3
"""Module Base"""

import json
import os


class Base:
    """first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor init"""

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

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes the JSON string representation of
        list_objs to a file"""

        newfile = "{}.json".format(cls.__name__)
        dicct = []

        if list_objs is not None:
            for i in list_objs:
                dicct.append(cls.to_dictionary(i))

        with open(newfile, "w", encoding="UTF8") as lista:
            lista.write(cls.to_json_string(dicct))

    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of the JSON string
        representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Square":
            dummy = cls(5)
            dummy.update(**dictionary)
            return dummy

        if cls.__name__ == "Rectangle":
            dummy = cls(8, 4)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """"Returns a a list of instances"""

        newfile = "{}.json".format(cls.__name__)
        lista = []

        if os.path.isfile(newfile):
            with open(newfile, encoding="utf-8") as new:
                items = cls.from_json_string(new.read())
            for i in items:
                lista.append(cls.create(**i))
            return lista
        else:
            return []
