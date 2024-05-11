#!/usr/bin/python3
"""
Module for defining a Student class with JSON serialization and deserialization methods.
"""

class Student:
    """
    A class to represent a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to be included in the dictionary.
                If None, all attributes are included.

        Returns:
            dict: A dictionary representing the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on the provided dictionary.

        Args:
            json (dict): A dictionary containing attribute-value pairs.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
