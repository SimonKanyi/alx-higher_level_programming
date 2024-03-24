#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position.

    Args:
        my_list (list): The list in which to replace the element.
        idx (int): The index at which to replace the element.
        element: The new element to replace at the specified index.

    Returns:
        The modified list with the element replaced, or the original list if idx
        is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
