#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argvlen = len(sys.argv)

    plural = "" if argvlen == 2 else "s"
    sep = "." if argvlen == 1 else ":"
    print("{} argument{}{}".format(argvlen - 1, plural, sep))
    for i in range(1, argvlen):
        print("{}: {}".format(i, sys.argv[i]))
