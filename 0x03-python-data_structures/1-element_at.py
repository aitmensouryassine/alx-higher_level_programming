#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0 or idx >= len(my_list)):
        return None
    else:
        for i, num in enumerate(my_list):
            if idx == i:
                print("Element at index {} is {:d}".format(i, num))
