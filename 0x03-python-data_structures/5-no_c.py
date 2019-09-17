#!/usr/bin/python3
def no_c(my_string):
    noc = []
    for i in my_string:
        if i != 'c' and i != 'C':
            noc.append(i)
        return "".join(noc)
