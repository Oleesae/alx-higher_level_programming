#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # get the lengths of the tuples
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a == 0: #if tuple is empty, let both values equal 0
        a1 = 0
        a2 = 0
    elif len_a == 1: #let missing value equal 0
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if len_b == 0:
        b1 = 0
        b2 = 0
    elif len_b == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]
        #return only first two values of tuple
        new_tuple = (a1 + b1, a2 + b2)

        return (new_tuple)
