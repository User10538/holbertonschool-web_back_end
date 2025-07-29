#!/usr/bin/env python3
"""
This module defines and annotate the following variables
with the specified values.
"""


def a(n: int):
    """
    an integer with a value of 1

    Args:
    n: int.

    Returns:
    Value of 1
    """
    if not isinstance(n, int):
        raise TypeError("n must be a integer")
    n = 1

    return n


def pi(n: float):
    """
    a float with a value of 3.14

    Args:
    n: float.

    Returns:
    value of 3.14
    """

    if not isinstance(n, float):
        raise TypeError("n must be a float")
    n = 3.14

    return n


def i_understand_annotations(n: bool):
    """
    a boolean with a value of True

    Args:
    n: boolean

    Returns:
    Value of true
    """
    if not isinstance(n, bool):
        raise TypeError("n must be a boolean")

    return n


def school(n: str):
    """
    a string with a value of “Holberton”

    Args:
    n: String.

    Returns:
    Value of “Holberton”
    """
    if not isinstance(n, str):
        raise TypeError("n must be a String")

    return n
