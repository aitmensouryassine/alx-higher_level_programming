#!/usr/bin/python3
for ascii in range((97 + 25), 96, -1):
    if ascii % 2 == 0:
        print("{ascii:c}".format(ascii=ascii), end="")
    else:
        print("{ascii:c}".format(ascii=ascii - (97 - 65)), end="")
