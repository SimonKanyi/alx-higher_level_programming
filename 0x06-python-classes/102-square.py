#!/usr/bin/python3
"""
This module defines a Square class that represents a square.
"""

class Square:
    """
    A class representing a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square with a given size.
        """
        self.size = size

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
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two squares are equal.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two squares are not equal.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Checks if one square is less than another.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if one square is less than or equal to another.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Checks if one square is greater than another.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if one square is greater than or equal to another.
        """
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
