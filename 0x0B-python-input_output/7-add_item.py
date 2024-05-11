#!/usr/bin/python3
"""
Script to add all arguments to a Python list and save them to a file in JSON format.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

try:
    # Load existing data from file, if any
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    # If file doesn't exist, start with an empty list
    data = []

# Add command line arguments to the list
data.extend(sys.argv[1:])

# Save the updated list to file
save_to_json_file(data, "add_item.json")
