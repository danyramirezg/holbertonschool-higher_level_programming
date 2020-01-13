#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)."""

import urllib.request
from sys import argv

if __name__ == "__main__":

    req = urllib.request.Request(argv[1])
    try:
        urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
