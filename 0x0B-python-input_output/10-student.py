#!/usr/bin/python3
"""
This module contain a class Student that defines a student
"""


class Student:
    """ A student class

    Instantiation with first_name, last_name and age

    Args:
        first_name (str): first name
        last_name (str): last name
        age (int): age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        A JSON representation of an object

        Args:
            attrs (:obj: list[str], optional): attribute name  to be retrieved.
        Returns:
            str: the dictionary description
        """
        if attrs is not None:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        else:
            return dict(self.__dict__)
