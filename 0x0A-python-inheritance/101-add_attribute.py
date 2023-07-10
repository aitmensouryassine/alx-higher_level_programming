#!/usr/bin/python3
""" add attr module """


def add_attribute(obj, attr_name, attr_value):
    """ adds an attribute to an obj if possible """

    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
