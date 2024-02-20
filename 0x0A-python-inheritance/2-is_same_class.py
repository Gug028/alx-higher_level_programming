#!/usr/bin/python3
"""Return instance of a specific class."""


def is_same_class(obj, a_class):
    """Check if an object is instance of a given class.
    Args:
        obj (any): The object to check.
        a_class (type): he class to compare the type of obj to.
    Returns:
        Boolean of an instance of a_class.
    """
    if type(obj) == a_class:
        return True
    return False
