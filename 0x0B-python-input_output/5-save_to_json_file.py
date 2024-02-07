#!/usr/bin/python3
"""
This module contain a function that writes an Object
to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation

    Args:
        filename (str): the name of the file
        my_obj (object): an object to serialized
    """
    with open(filename, 'w') as filename:
        json.dump(my_obj, filename)
