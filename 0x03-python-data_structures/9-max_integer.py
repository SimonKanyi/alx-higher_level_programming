#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the biggest integer of a list.

    Args:
        my_list (list): The input list.

    Returns:
        The biggest integer in the list, or None if the list is empty.
    """
    if len(my_list) == 0:
        return None

    max_val = my_list[0]
    for num in my_list:
        if num > max_val:
            max_val = num

    return max_val
