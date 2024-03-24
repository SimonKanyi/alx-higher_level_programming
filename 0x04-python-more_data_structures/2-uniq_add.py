#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unique integers in a list (only once for each integer).

    Args:
        my_list (list): The list of integers.

    Returns:
        int: The sum of all unique integers in the list.

    """
    unique_numbers = set(my_list)
    return sum(unique_numbers)

# Test the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
