#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key (str): The key to delete.

    Returns:
        dict: The updated dictionary.

    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

# Test the function
if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
    new_dict = simple_delete(a_dictionary, 'track')
    print(a_dictionary)
    print("--")
    print(new_dict)

    print("--")
    print("--")
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print(a_dictionary)
    print("--")
    print(new_dict)
