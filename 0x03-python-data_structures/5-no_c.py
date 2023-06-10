#!/usr/bin/python3
def no_c(my_string):
    list = []

    for char in my_string:
        if char != "C" and char != "c":
            list.append(char)

    return ''.join(list)
