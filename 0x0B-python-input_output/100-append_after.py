#!/usr/bin/python3
""" Search and update """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line
    ontaining a specific string """

    my_list = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            my_list.append(line)
            if search_string in line:
                my_list.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(my_list))
