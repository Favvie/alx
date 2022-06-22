#!/usr/bin/python3
""" the class square module"""

class Square:
    """ initializing the square class """
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
        def size(self,value):
            if type(self, size):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

    def area(self):
        return self.__size * self.__size
