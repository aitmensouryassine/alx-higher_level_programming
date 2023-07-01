#!/usr/bin/python3
""" Print square Module """


def print_square(size):
    """ prints a square with # symbol """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
