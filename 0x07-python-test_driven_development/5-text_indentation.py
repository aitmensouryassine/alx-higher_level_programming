#!/usr/bin/python3
""" Text indentation module """


def text_indentation(text):
    """ prints a text with 2 new lines
    after each of these characters: ., ? and : """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = []
    line = []
    new_line = True

    for c in text:
        if new_line and c == " ":
            continue
        else:
            if c == "?" or c == "." or c == ":":
                line.append(c)
                line.append("\n\n")
                lines.append(line)
                line = []
                new_line = True
            elif c == "\n":
                line.append("\n")
                lines.append(line)
                line = []
                new_line = True
            else:
                line.append(c)
                new_line = False

    if not line in lines:
        lines.append(line)

    for line in lines:
        for char in line:
            print(char, end="")
