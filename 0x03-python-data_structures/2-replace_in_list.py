#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # if idx is negative
    if idx < 0:
        return (my_list)
    # if idx is out of range of my_list
    if idx >= len(my_list):
        return (my_list)
    my_list[idx] = element
