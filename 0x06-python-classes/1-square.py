#!/usr/bin/python3
"""Defines a square and a Private instance attribute with size"""


class Square:
    """create Square type"""

    def __init__(self, size):
        """Initailizes Square with size"""

        self.__size = size
