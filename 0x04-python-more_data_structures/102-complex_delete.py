#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dictionary = {key: val for key, val in a_dictionary.items() if val != value}
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return new_dictionary

