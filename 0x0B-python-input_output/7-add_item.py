#!/usr/bin/python3
"""This module loads a list, saves the updated list to a JSON file"""
from sys import argv


load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

try:
    arg_list = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    arg_list = []

for item in argv[1:]:
    arg_list.append(item)

save_file(arg_list, 'add_item.json')
