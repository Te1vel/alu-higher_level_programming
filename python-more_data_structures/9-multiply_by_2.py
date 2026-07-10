#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return {}
    return {key: value * 2 for key, value in a_dictionary.items()}
