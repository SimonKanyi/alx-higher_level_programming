#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list.

    Args:
        my_list (list): The input list.

    Returns:
        A new list containing True or False, depending on whether the integer at
        the same position in the original list is a multiple of 2.
    """
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
