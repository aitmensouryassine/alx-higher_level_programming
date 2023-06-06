#!/usr/bin/python3
for n in range(0, 100):
    if n < 99:
        print("{n:02}".format(n=n), end=", ")
    else:
        print("{n:02}".format(n=n))
