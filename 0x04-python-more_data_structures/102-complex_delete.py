#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list = []
    for key, val in a_dictionary.items():
        if val == value:
            list.append(key)
    for key in list:
        del a_dictionary[key]

    return a_dictionary
