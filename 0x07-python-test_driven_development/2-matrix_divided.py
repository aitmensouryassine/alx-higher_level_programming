#!/usr/bin/python3
""" Matrix division Module """


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    for row in matrix:
        if not all((isinstance(col, int) or
                    isinstance(col, float)) for col in row):
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda row:
                    list(map(lambda col: round(col/div, 2), row)), matrix))
