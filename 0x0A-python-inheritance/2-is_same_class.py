#!/usr/bin/python3
""" Is same class module """


def is_same_class(obj, a_class):
    """ checks if an object is an instance of a class """

    return obj.__class__.__name__ == a_class.__name__
