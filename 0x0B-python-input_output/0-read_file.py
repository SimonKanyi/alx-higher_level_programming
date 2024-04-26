#!/usr/bin/python3

def read_file(filename=""):
    """
    Read and print the contents of a text file to stdout.

    Args:
        filename (str): The name of the file to be read. Defaults to empty string.

    Returns:
        None
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')

# Example usage
if __name__ == "__main__":
    read_file("my_file_0.txt")
