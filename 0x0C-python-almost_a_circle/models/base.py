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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w+", encoding="utf-8") as f:
            if list_objs is None:
                json_str = "[]"
            else:
                json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            f.write(json_str)
