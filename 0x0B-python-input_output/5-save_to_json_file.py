#!/usr/bin/python3
<<<<<<< HEAD
"""
Module for saving an object to a text file using JSON representation.
"""

=======
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
import json

def save_to_json_file(my_obj, filename):
    """
<<<<<<< HEAD
    Saves an object to a text file using JSON representation.

    Args:
        my_obj: The object to be saved.
        filename (str): The name of the file to save to.
=======
    Write an object to a text file using JSON representation.

    Args:
        my_obj (object): The object to be saved to the file.
        filename (str): The name of the file to save the JSON representation.
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f

    Returns:
        None
    """
<<<<<<< HEAD
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
=======
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

# Example usage
if __name__ == "__main__":
    filename = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename)

    filename = "my_dict.json"
    my_dict = { 
        'id': 12,
        'name': "John",
        'places': [ "San Francisco", "Tokyo" ],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    save_to_json_file(my_dict, filename)

    try:
        filename = "my_set.json"
        my_set = { 132, 3 }
        save_to_json_file(my_set, filename)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
