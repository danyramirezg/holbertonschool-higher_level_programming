#!/usr/bin/python3

import sys

"""script that adds all arguments to a Python list,
and then save them to a file"""

save_to_json = __import__('7-save_to_json_file').save_to_json_file
load_from_json = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        list = load_from_json("add_item.json")
    except:
        pass
        list = []
    for arg in sys.argv[1:]:
        list.append(arg)
    save_to_json(list, "add_item.json")
