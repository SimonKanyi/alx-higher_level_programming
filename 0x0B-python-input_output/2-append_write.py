#!/usr/bin/python3
<<<<<<< HEAD
"""
Module for writing a string to a text file and returning the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        num_characters_written = file.write(text)
    
    return num_characters_written


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
=======

def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8) and return the number of characters added.

    Args:
        filename (str): The name of the file to append to. Defaults to empty string.
        text (str): The text to append to the file. Defaults to empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
    return nb_characters_added

# Example usage
if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
