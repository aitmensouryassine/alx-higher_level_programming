#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < (97 + 26):
            ascii = ord(str[i]) - (97 - 65)
        else:
            ascii = ord(str[i])

        print("{ascii:c}".format(ascii = ascii), end="")
    print()
