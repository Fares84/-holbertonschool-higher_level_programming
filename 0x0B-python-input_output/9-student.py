#!/usr/bin/python3
""" class Student that defines a student """


class Student:
    """ defining a student class """

    def __init__(self, first_name, last_name, age):
        """ initialisation of the student class and
        defining attributs

        Arguments:
            first_name {[str]} -- [first name]
            last_name {[str]} -- [last name]
            age {[int]} -- [age of student]
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance

        Returns:
            (dict) -- [dictionnary holding description of object]
        """
        return self.__dict__
