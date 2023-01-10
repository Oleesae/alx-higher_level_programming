#!/usr/bin/python3
def element_at(my_list, idx):
    # if idx is negative
    if idx < 0:
        return (None)
    # if idx is out of range of my_list
    if idx >= len(my_list):
        return (None)
    return my_list.copy().pop(idx)
    
