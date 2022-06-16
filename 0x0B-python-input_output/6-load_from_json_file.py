#!/usr/bin/python3
"""load_from_json_file function"""


import json


def load_from_json_file(filename):
    """a function that creates an Object from a JSON file"""
    with open(filename, 'r', encoding="utf-8") as fd:
        return json.load(fd)
