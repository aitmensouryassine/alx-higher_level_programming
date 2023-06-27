#!/usr/bin/python3
""" MagicClass Module """
import math


class MagicClass:
    """ Represent a circle """

    def __init__(self, radius):
        """ Init a circle """
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """ Return the area of a circle """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Return the circumference of a circle """
        return 2 * math.pi * self.__radius
