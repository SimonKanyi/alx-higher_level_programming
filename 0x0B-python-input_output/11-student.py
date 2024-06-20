#!/usr/bin/python3
<<<<<<< HEAD
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
=======

class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first name, last name, and age."""
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
<<<<<<< HEAD
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to be included in the dictionary.
                If None, all attributes are included.

        Returns:
            dict: A dictionary representing the Student instance.
        """
=======
        """Return a dictionary representation of the Student instance based on attrs."""
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
<<<<<<< HEAD
        """
        Replaces all attributes of the Student instance based on the provided dictionary.

        Args:
            json (dict): A dictionary containing attribute-value pairs.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
=======
        """Replace all attributes of the Student instance based on the provided JSON."""
        for key, value in json.items():
            setattr(self, key, value)

# Example usage
if __name__ == "__main__":
    # Sample usage as described in 11-main.py
    student_1 = Student("John", "Doe", 23)
    j_student_1 = student_1.to_json()
    print("Initial student:")
    print(student_1)
    print(type(student_1))
    print(type(j_student_1))
    print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))

    # Simulating saving and loading from JSON file
    path = "student.json"
    save_to_json_file(j_student_1, path)
    new_j_student_1 = load_from_json_file(path)

    # Creating a new Student instance and reloading from JSON
    new_student_1 = Student("Fake", "Fake", 89)
    print("Fake student:")
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

    new_student_1.reload_from_json(new_j_student_1)
    print("Reloaded student:")
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
>>>>>>> 02761f485d7ed4b53728a076f42cc8a0fd0f711f
