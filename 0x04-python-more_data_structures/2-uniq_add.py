#!/usr/bin/python3
def uniq_add(my_list=[]):
    val = []
    total = 0
    for i in range(len(my_list)):
        if my_list[i] not in val:
            total += my_list[i]
            val.append(my_list[i])
    return (total)
