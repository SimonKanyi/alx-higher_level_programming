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

<<<<<<< HEAD
    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representing the Student instance.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
=======
    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

# Example usage
if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
