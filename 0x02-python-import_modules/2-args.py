#!/usr/bin/python3
import sys

argvlen = len(sys.argv)

if argvlen == 1:
    print("0 arguments.")
else:
    print(argvlen - 1, "arguments:")
    for i in range(1, argvlen):
        print("{}: {}".format(i, sys.argv[i]))
