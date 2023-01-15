#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dsort = sorted(a_dictionary)
    for i in range(len(dsort)):
        if dsort[i] in a_dictionary:
            print("{}: {}".format(dsort[i], a_dictionary[dsort[i]]))
