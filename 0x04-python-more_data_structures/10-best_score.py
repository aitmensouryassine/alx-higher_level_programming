#!/usr/bin/python3
def best_score(a_dictionary):
    best = None
    score = 0
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > score:
                score = v
                best = k

    return best
