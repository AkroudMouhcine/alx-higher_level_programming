#!/usr/bin/python3
"""Defines a function to check object class."""


def is_same_class(obj, a_class):
    """
    Verify whether an object is exactly an instance of a specified class.

    Args:
        obj (any): The object to validate.
        a_class (type): The class for comparison.

    Returns:
        True if obj is exactly an instance of a_class, otherwise returns False.
    """
    if type(obj) == a_class:
        return True
    return False
