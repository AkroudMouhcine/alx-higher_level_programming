#!/usr/bin/python3
"""
Class definition for MyList, a subclass of list.

Attributes:
    None.

Methods:
    print_sorted(): Prints the list in ascending sorted order.
"""
class MyList(list):
    """
    Class definition for MyList, a subclass of list.
    """

    def print_sorted(self):
        """
        Prints the list in sorted ascending order.
        """
        print(sorted(self))
