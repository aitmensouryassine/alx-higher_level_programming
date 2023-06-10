#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        biggest = my_list[0]
        for num in my_list:
            biggest = num if num > biggest else biggest
        return biggest
    else:
        return None
