#!/usr/bin/python3
"""
This module defines a Square class that represents a square.
"""

class Square:
    """
    A class representing a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square with a given size and position.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(x, int) for x in value) or \
           not all(x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Computes and returns the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        string_repr = ""
        if self.__size == 0:
            return string_repr
        for _ in range(self.__position[1]):
            string_repr += "\n"
        for _ in range(self.__size):
            string_repr += " " * self.__position[0] + "#" * self.__size + "\n"
        return string_repr.rstrip()


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
