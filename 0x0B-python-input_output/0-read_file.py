#!/usr/bin/python3
<<<<<<< HEAD
"""
Module for reading and printing the content of a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
=======

def read_file(filename=""):
    """
    Read and print the contents of a text file to stdout.

    Args:
        filename (str): The name of the file to be read. Defaults to empty string.
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f

    Returns:
        None
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')

<<<<<<< HEAD

=======
# Example usage
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
if __name__ == "__main__":
    read_file("my_file_0.txt")
