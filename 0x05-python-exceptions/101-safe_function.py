#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    x, y = args
    try:
        result = fct(x, y)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return result
    else:
        return result
