#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list.

    Args:
        my_list (list): The input list.
        idx (int): The index of the item to delete.

    Returns:
        The modified list with the item at the specified index removed, or the original list if idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
    return my_list
