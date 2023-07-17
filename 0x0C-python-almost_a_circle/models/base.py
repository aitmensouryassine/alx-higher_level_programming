#!/usr/bin/python3
""" Base Module """
import json
import csv
import turtle


class Base():
    """ Base class: manage id attribute in all your future classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def reset(cls):
        """ reset number of objs to zero """
        cls.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w+", encoding="utf-8") as f:
            if list_objs is None:
                json_str = "[]"
            else:
                obj_list = [obj.to_dictionary() for obj in list_objs]
                json_str = cls.to_json_string(obj_list)
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                obj = cls(1)
            elif cls.__name__ == "Rectangle":
                obj = cls(1, 1)

            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances loaded from a file """
        filename = cls.__name__ + ".json"

        try:
            f = open(filename, "r", encoding="utf-8")
            json_string = f.read()
            dictionaries = cls.from_json_string(json_string)
            f.close()
            return [cls.create(**dic) for dic in dictionaries]
        except FileNotFoundError:
            return []

    @staticmethod
    def get_field_names(cls_name):
        """ returns the field names for a given class """
        if cls_name == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        else:
            return ["id", "size", "x", "y"]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes in CSV """
        filename = cls.__name__ + ".csv"

        with open(filename, 'w+', newline='') as csvf:
            if list_objs is None or list_objs == []:
                csvf.write("[]")
            else:
                fieldnames = cls.get_field_names(cls.__name__)
                writer = csv.DictWriter(csvf,
                                        fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes in CSV """
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, "r", newline="") as csvf:
                fieldnames = cls.get_field_names(cls.__name__)
                list_dicts = csv.DictReader(csvf,
                                            fieldnames=fieldnames)
                list_dicts = [{key: int(value) for key, value in dic.items()}
                              for dic in list_dicts]
                return [cls.create(**dic) for dic in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ opens a window and draws all the Rectangles and Squares """
        wndw = turtle.Screen()
        wndw.bgcolor("#000000")
        wndw.title("Rectangles & Squares")

        ttl = turtle.Turtle()
        ttl.screen.bgcolor("#000000")
        ttl.shape("turtle")

        ttl.color("#ff0000")
        for sq in list_squares:
            ttl.showturtle()
            ttl.up()
            ttl.goto(sq.x, sq.y)
            ttl.down()
            for i in range(4):
                ttl.forward(sq.size)
                ttl.left(90)
            ttl.hideturtle()

        ttl.color("#00ff00")
        for rect in list_rectangles:
            ttl.showturtle()
            ttl.up()
            ttl.goto(rect.x, rect.y)
            ttl.down()
            for i in range(2):
                ttl.forward(rect.width)
                ttl.left(90)
                ttl.forward(rect.height)
                ttl.left(90)
            ttl.hideturtle()

        turtle.exitonclick()
