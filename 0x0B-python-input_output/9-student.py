#!/usr/bin/python3
<<<<<<< HEAD
"""
Module for defining a Student class.
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
=======

class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first name, last name, and age."""
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
<<<<<<< HEAD
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representing the Student instance.
        """
=======
        """Return a dictionary representation of the Student instance."""
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
<<<<<<< HEAD
=======

# Example usage
if __name__ == "__main__":
    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
