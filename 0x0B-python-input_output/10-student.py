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
        s_dict = {}
        if type(attrs) == list and type(attrs[0]) == str:
            for key in attrs:
                if hasattr(self, key):
                    s_dict[key] = self.__dict__[key]
        else:
            s_dict = self.__dict__
        return dict(s_dict)
