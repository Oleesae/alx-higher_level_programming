#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key in a_dictionary or key not in a_dictionary:
        a_dictionary[key] = value
