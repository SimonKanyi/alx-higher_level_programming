#!/usr/bin/python3
"""
Module for converting an object to its JSON representation.
"""

import json

def to_json_string(my_obj):
    """
    Converts an object to its JSON representation.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
