#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = []

    for num in my_list:
        list.append(True) if num % 2 == 0 else list.append(False)

    return list
