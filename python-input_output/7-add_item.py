#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a JSON file."""
import json
import sys

filename = "add_item.json"

try:
    with open(filename, 'r') as f:
        list_items = json.load(f)
except FileNotFoundError:
    list_items = []

list_items.extend(sys.argv[1:])

with open(filename, 'w') as f:
    json.dump(list_items, f)
