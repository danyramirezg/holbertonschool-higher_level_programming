#!/usr/bin/python3
def uniq_add(my_list=[]):
    count = 0
    new_list = set(my_list)
    for i in new_list:
        count += i
    return count
