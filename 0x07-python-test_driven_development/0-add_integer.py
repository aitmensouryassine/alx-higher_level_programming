#!/usr/bin/python3
""" A module for 0x07 project (python: test driven development) """


def add_integer(a, b=98):
    """ A function that adds two integers
    If floats were passed, we cast them to integers
    If args are not of type int or float we raise TypeError """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
