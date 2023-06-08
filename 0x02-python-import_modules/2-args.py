#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argvlen = len(sys.argv)

    if argvlen == 1:
        print("0 arguments.")
    else:
        plural = "" if argvlen <= 2 else "s"
        print("{} argument{}:".format(argvlen - 1, plural))
        for i in range(1, argvlen):
            print("{}: {}".format(i, sys.argv[i]))
