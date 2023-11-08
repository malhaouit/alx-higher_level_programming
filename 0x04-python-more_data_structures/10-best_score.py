#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        max_value = max({a_dictionary.get(key) for key in a_dictionary})
        for k in a_dictionary:
            if a_dictionary.get(k) == max_value:
                return k
    return None
