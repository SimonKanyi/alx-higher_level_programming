#!/usr/bin/python3
""" Module for Base class """

class Base:
    """ Base class for managing id attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes a Base instance """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
