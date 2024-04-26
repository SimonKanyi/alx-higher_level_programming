#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to empty string.
        text (str): The text to write to the file. Defaults to empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters

# Example usage
if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
