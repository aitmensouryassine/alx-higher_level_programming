#!/usr/bin/python3
""" Is kind of class module """


def is_kind_of_class(obj, a_class):
    """ checks if an object is an instance of a class
     or is an instance of a class that inherited from """

    return isinstance(obj, a_class)
