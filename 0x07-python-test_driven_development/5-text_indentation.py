#!/usr/bin/python3
"""Function that prints a text with 2 new
lines after each
of these characters: ., ? and :

"""


def text_indentation(text):
    """There should be no space at the beginning or
     at the end of each printed line
     """

    if text is None:
        return None
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == " " and text[i + 1] == " ":
            continue
        if text[i] is " " and (text[i - 1] is "." or text[i - 1] is "?" or
                               text[i - 1] is ":" or text[i - 1] is " "):
            continue
        print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print()
            print()
