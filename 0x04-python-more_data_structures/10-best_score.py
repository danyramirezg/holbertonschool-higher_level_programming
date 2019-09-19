#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        name = " "
        score = 0
    for x in a_dictionary:
        if a_dictionary[x] > score:
            name = x
            score = a_dictionary[x]
    return name
