#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # if idx is negative and is out of range of my_list
    if 0 <= idx < len(my_list):
        new_list = my_list.copy()
        new_list[idx] = element
    return (my_list)
