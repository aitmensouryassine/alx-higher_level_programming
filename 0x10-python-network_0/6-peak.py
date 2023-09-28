#!/usr/bin/python3
"""module contains a function that finds a peak in a
list of unsorted integers
"""


def find_peak(list_of_integers):
    """function that finds the peak in a list"""
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    middle = int(length / 2)
    peak = list_of_integers[middle]
    if peak > list_of_integers[middle - 1] and \
            peak > list_of_integers[middle + 1]:
        return peak
    elif peak < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[:middle])
    else:
        return find_peak(list_of_integers[middle + 1:])
