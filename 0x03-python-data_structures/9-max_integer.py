#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = 0
    if my_list:
        for num in my_list:
            biggest = num if num > biggest else biggest
        return biggest
    else:
        return None
