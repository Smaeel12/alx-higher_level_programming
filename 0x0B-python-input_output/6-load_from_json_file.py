#!/usr/bin/python3
"""
This module contain a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”

    Args:
        filename (str): the file path

    Returns:
        object: Python data structure
    """
    with open(filename) as filename:
        return json.load(filename)
