#!/usr/bin/python3
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
