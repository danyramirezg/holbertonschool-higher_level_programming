#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        temp = fct(*args)
        return temp
    except Exception as exc:
        stderr.write("Exception: {}\n".format(exc))
        return None
