#!/usr/bin/python3
""" MyInt Module """


class MyInt(int):
    """ MyInt Class """

    def __ne__(self, other):
        return super().__eq__(other)

    def __eq__(self, other):
        return super().__ne__(other)
