#!/usr/bin/python3
""" MyList Module """


class MyList(list):
    """ MyList Class """

    def print_sorted(self):
        t = self[:]
        t.sort()
        print(t)
