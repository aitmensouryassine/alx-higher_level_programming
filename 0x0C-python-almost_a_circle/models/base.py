#!/usr/bin/python3
""" Base Module """
import json


class Base():
    """ Base class: manage id attribute in all your future classes """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def reset(cls):
        cls.__nb_objects = 0

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
