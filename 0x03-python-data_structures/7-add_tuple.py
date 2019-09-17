#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return
    elem1 = tuple_a + ('0', '0')
    elem2 = tuple_b + ('0', '0')

    result1 = int(elem1[0]) + int(elem2[0])
    result2 = int(elem1[1]) + int(elem2[1])
    return(result1), (result2)
