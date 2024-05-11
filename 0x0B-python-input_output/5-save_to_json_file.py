#!/usr/bin/python3
"""
Module for saving an object to a text file using JSON representation.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Saves an object to a text file using JSON representation.

    Args:
        my_obj: The object to be saved.
        filename (str): The name of the file to save to.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
