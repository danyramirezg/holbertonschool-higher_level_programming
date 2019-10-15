#!/usr/bin/python3
"""class MyList that inherits from list"""


class List:
    pass


class MyList(list):
    def print_sorted(self):
        new = self.copy()
        new.sort()
        print(new)
