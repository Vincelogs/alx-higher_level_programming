#!/usr/bin/python3
"""Function to add to integer"""


def add_integer(a, b=98):
    """
    Add two integers.
    Args:
        a: The first integer.
        b: The second integer (default: 98).
    Returns:
        The sum of a and b.
    Raises:
        TypeError: if a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
