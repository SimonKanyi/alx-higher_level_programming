#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters 'c' and 'C' from a string.

    Args:
        my_string (str): The input string.

    Returns:
        The new string with all occurrences of 'c' and 'C' removed.
    """
    result = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            result += char
    return result
