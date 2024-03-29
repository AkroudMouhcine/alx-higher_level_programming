#!/usr/bin/python3
"""
Includes the inherits_from function.
"""


def inherits_from(obj, a_class):
    """Returns True if obj is a subclass of a_class, else False."""
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
