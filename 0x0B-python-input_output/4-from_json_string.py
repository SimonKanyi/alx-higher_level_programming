#!/usr/bin/python3
<<<<<<< HEAD
"""
Module for converting a JSON string to an object (Python data structure).
"""

=======
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
import json

def from_json_string(my_str):
    """
<<<<<<< HEAD
    Converts a JSON string to an object (Python data structure).

    Args:
        my_str (str): The JSON string to be converted.
=======
    Return an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted to an object.
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
<<<<<<< HEAD
=======

# Example usage
if __name__ == "__main__":
    s_my_list = "[1, 2, 3]"
    my_list = from_json_string(s_my_list)
    print(my_list)
    print(type(my_list))

    s_my_dict = """
    {"is_active": true, "info": {"age": 36, "average": 3.14}, 
    "id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))

    try:
        s_my_dict = """
        {"is_active": true, 12 }
        """
        my_dict = from_json_string(s_my_dict)
        print(my_dict)
        print(type(my_dict))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
