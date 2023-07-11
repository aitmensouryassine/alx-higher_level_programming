#!/usr/bin/python3
""" Write to file module """


def write_file(filename="", text=""):
    """ writes text to file """

    with open(filename, "w+", encoding="utf-8") as f:
        return f.write(text)
