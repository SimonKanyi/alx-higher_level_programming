#!/usr/bin/python3

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
