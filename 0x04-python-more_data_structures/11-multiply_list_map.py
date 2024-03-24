#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """Returns a new list with all values multiplied by a number using map.

    Args:
        my_list (list): The input list.
        number (int): The number to multiply each value by.

    Returns:
        list: A new list with each value multiplied by the given number.

    """
    return list(map(lambda x: x * number, my_list))

# Test the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 6]
    new_list = multiply_list_map(my_list, 4)
    print(new_list)
    print(my_list)
