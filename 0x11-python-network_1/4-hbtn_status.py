#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status, using
 the package requests
"""

import requests

res = requests.get('https://intranet.hbtn.io/status')

print("Body response:")
print("\t- type: {}".format(type(res.text)))
print("\t- content: {}".format(res.text))
