#!/usr/bin/python3
"""
This module contain a function that returns the JSON representation
of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    a function that returns the JSON representation of an object (string)

    Args:
        my_obj (object): an object (string)

    Returns:
        str: returns the JSON representation
    """
    return json.dumps(my_obj)
