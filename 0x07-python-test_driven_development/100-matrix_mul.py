#!/usr/bin/python3
""" Matrix multiplication module """


def matrix_mul(m_a, m_b):
    """ Multplies two matrices """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(type(row) is list for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(type(row) is list for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or all(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or all(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if not all(type(col) in [int, float] for col in row):
            raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not all(type(col) in [int, float] for col in row):
            raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    a_rows = len(m_a)
    a_cols = len(m_a[0])
    b_rows = len(m_b)
    b_cols = len(m_b[0])
    if a_cols != b_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    matrix = []
    for i in range(a_rows):
        matrix.append([])
    for row in matrix:
        for i in range(b_cols):
            row.append(0)

    res = 0
    for j in range(b_cols):
        for i in range(a_rows):
            for k in range(b_rows):
                res = res + (m_a[i][k] * m_b[k][j])
            matrix[i][j] = res
            res = 0

    return matrix
