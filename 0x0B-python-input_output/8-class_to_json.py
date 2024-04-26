#!/usr/bin/python3

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
