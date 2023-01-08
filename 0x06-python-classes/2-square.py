#!/usr/bin/python3
"""Defines a square and a Private instance attribute with size"""

class Square:
    """create Square type"""
    def __init__(self, size=0):
        """Initailizes Square with size"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")	    
