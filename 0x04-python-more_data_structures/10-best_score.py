#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_key = None
        best_value = float('-inf')

        for key, value in a_dictionary.items():
            if value > best_value:
                best_key = key
                best_value = value

        return best_key
    else:
        return None