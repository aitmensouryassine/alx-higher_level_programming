#!/usr/bin/python3
def islower(c):
    """Return True if character c is lowercase, False otherwise"""
    if ord(c) >= 97 and ord(c) < (97 + 26):
        return True
    else:
        return False
