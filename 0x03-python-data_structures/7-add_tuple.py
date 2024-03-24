#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples.

    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.

    Returns:
        A tuple containing the sum of corresponding elements from tuple_a and tuple_b.
    """
    # If a tuple is smaller than 2, use the value 0 for each missing integer
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    # If a tuple is bigger than 2, use only the first 2 integers
    return (a[0] + b[0], a[1] + b[1])
