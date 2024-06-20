#!/usr/bin/python3
<<<<<<< HEAD
"""
Module for converting an object to its JSON representation.
"""

def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary description of the object suitable for JSON serialization.
    """
    description = {}
    for attr in dir(obj):
        # Exclude private attributes and methods
        if not attr.startswith('__'):
            value = getattr(obj, attr)
            # Check if the attribute is serializable
            if isinstance(value, (list, dict, str, int, bool)):
                description[attr] = value
    return description
=======

def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: Dictionary representing the serialized object.
    """
    attributes = obj.__dict__
    return attributes
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
