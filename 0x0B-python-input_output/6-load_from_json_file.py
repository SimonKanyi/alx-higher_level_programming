#!/usr/bin/python3
<<<<<<< HEAD
"""
Module for loading an object from a JSON file.
"""

=======
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
import json

def load_from_json_file(filename):
    """
<<<<<<< HEAD
    Loads an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        object: The object loaded from the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
=======
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The object represented by the JSON content of the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)

# Example usage
if __name__ == "__main__":
    filename = "my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
    print(type(my_list))

    filename = "my_dict.json"
    my_dict = load_from_json_file(filename)
    print(my_dict)
    print(type(my_dict))

    try:
        filename = "my_set_doesnt_exist.json"
        my_set = load_from_json_file(filename)
        print(my_set)
        print(type(my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        filename = "my_fake.json"
        my_fake = load_from_json_file(filename)
        print(my_fake)
        print(type(my_fake))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
