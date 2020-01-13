#!/usr/bin/python3

"""Python script that fetches https://intranet.hbtn.io/status. Using
 the package urllib
"""

import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
    res = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
    print("\t- utf8 content: {}".format(res.decode("utf8")))
