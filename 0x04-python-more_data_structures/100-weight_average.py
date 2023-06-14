#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    total1, total2 = 0, 0

    for value, weight in my_list:
        total1 += value * weight
        total2 += weight
    if my_list:
        average = total1 / total2

    return average
