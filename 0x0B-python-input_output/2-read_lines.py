#!/usr/bin/python3

"""function that reads n lines of a text
file (UTF8) and prints it to stdout"""


def read_lines(filename="", nb_lines=0):

    """Read the entire file if nb_lines is
    lower or equal to 0 OR greater or equal to
    the total number of lines of the file"""

    with open(filename, encoding="UTF8") as text:
        count = 0
        for n in text:
            count += 1
            print(n, end="")
            if nb_lines == count:
                break
