#!/usr/bin/python3
"""This module loads, saves a list to the JSON file"""
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_list = load_from_json_file('add_item.json')

for arg in argv[1:]:
    arg_list.append(arg)

save_to_json_file(arg_list, 'add_item.json')
