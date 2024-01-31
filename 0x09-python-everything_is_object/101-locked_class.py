#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" This module a class LockedClass with no class or object attribute,
        that prevents the user from dynamically creating new instance
            attributes, except if the new instance attribute is
                called first_name.
"""


class LockedClass:
    """
    A locked class that only lets the user dynamically create the instance
    attribute 'first_name'
    """
    __slots__ = ['first_name']
