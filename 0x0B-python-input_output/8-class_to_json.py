#!/usr/bin/python3
"""
This module contain a function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean) for
JSON serialization of an object:
"""
import json


def class_to_json(obj):
    """ A JSON representation of an object

    Args:
        obj (object): An instance of a Class

    Returns:
        str: the dictionary description
    """
    return dict(vars(obj))
