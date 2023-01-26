#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    den = 0

    if not my:
        return 0
    for i in my_list:
        num += i[0] * i[1]
        den += i[1]

    return num / den
