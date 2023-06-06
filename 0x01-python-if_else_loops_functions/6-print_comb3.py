#!/usr/bin/python3
for n in range(0, 10):
    for x in range(n, 10):
        if n == 8 and x == 9:
            print("{n}{x}".format(n=n, x=x))
        elif n != x:
            print("{n}{x}, ".format(n=n, x=x), end="")
