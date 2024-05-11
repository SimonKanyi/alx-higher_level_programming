#!/usr/bin/python3
<<<<<<< HEAD
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
=======
import sys
from os import path
from json import dumps
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_items_to_list(items_list, filename="add_item.json"):
    """
    Adds items to a list and saves them to a JSON file.

    Args:
        items_list (list): List of items to add.
        filename (str): Name of the JSON file to save the list.

    Returns:
        None
    """
    if path.exists(filename):
        loaded_list = load_from_json_file(filename)
        items_list.extend(loaded_list)
    
    save_to_json_file(items_list, filename)

if __name__ == "__main__":
    args = sys.argv[1:]
    add_items_to_list(args)
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
