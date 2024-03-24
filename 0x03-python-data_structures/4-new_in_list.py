#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position without modifying the original list.

    Args:
        my_list (list): The original list.
        idx (int): The index at which to replace the element.
        element: The new element to replace at the specified index.

    Returns:
        A new list with the element replaced at the specified index, or a copy of the original list
        if idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
