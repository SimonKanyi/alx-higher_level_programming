<<<<<<< HEAD
#!/usr/bin/python3
"""
Module for appending a line of text to a file after each line containing a specific string.
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after each line containing the search string.

    Returns:
        None
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, mode='w', encoding='utf-8') as file:
=======
def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a specific string.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

<<<<<<< HEAD
# Example usage:
# append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
=======
# Testing the function
if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
