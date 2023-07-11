#!/usr/bin/python3
""" Pascal's Triangle """


def get_value(_list, i, j):
    """ gets a value from a list of lists if index is in range,
    if not retruns zero """

    if j + 1 == 0:
        return 0
    try:
        return _list[i][j]
    except Exception:
        return 0


def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal’s triangle of n """

    if n <= 0:
        return []

    pas_tri = [[1]]
    for i in range(1, n):
        row = []
        for j in range(i + 1):
            row.append(get_value(pas_tri, i - 1, j - 1) +
                       get_value(pas_tri, i - 1, j))
        pas_tri.append(row)

    return pas_tri
