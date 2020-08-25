#!/usr/bin/python3

"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter. """

import requests
import sys

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ''
    res = requests.post(url, data={'q': q}).json()

    try:
        result = res.json()
        if not result:
            print("No result")
        else:
            print('[{}] {}'.format(result.get('id'), result.get('name')))
    except ValueError:
        print("Not a valid JSON")
