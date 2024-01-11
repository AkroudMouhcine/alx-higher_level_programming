#!/usr/bin/python3
"""
Includes the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """True if obj is an instance or inherits from a_class, else False."""

    if isinstance(obj, a_class):
        return True
    return False
