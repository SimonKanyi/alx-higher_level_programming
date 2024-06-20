#!/usr/bin/python3
<<<<<<< HEAD
"""
Module for converting an object to its JSON representation.
"""

=======
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
import json

def to_json_string(my_obj):
    """
<<<<<<< HEAD
    Converts an object to its JSON representation.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
=======
    Return the JSON representation of an object as a string.

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3]
    s_my_list = to_json_string(my_list)
    print(s_my_list)
    print(type(s_my_list))

    my_dict = {
        'id': 12,
        'name': "John",
        'places': ["San Francisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    s_my_dict = to_json_string(my_dict)
    print(s_my_dict)
    print(type(s_my_dict))

    try:
        my_set = {132, 3}
        s_my_set = to_json_string(my_set)
        print(s_my_set)
        print(type(s_my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
