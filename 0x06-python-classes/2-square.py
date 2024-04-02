#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    A class representing a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square with a given size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
