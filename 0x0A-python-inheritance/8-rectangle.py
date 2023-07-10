#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Rectangle module """


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        self.integer_validator(width)
        self.integer_validator(height)
        self.width = width
        self.height = height
