#!/usr/bin/python3
"""Script to add all arguments to a Python list and save them to a file"""

import sys
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, "add_item.json")
