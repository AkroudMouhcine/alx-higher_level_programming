#!/usr/bin/python3
"""
Get a list of an object's attributes.

Parameters:
    obj: The object to inspect.

Returns:
    list: A list of available attributes
"""


def lookup(obj):
    """ Return a list of an object's available attributes. """
    return dir(obj)
