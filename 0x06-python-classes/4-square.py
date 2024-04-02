#!/usr/bin/python3
"""
This module defines a Square class with getter and setter methods for size.
"""


class Square:
    """
    A class representing a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square with a given size.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes the area of the square.
        """
        return self.__size ** 2
