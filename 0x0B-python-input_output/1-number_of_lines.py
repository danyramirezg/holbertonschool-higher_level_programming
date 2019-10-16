#!/usr/bin/python3

"""Function that returns the
number of lines of a text file"""


def number_of_lines(filename=""):
    with open(filename, encoding="UTF8") as text:
        count = 0
        for lines in text:
            count += 1
    return count
