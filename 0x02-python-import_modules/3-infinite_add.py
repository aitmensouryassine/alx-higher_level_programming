#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argvlen = len(sys.argv)
    sum = 0

    for i in range(1, argvlen):
        sum += int(sys.argv[i])

    print(sum)
