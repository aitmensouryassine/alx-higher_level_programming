#!/usr/bin/python3
""" Read file module """


def read_file(filename=""):
    """ Reads a file and print it to stdout """

    with open(filename, encoding="UTF-8") as f:
        print(f.read())
