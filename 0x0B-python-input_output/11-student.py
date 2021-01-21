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

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance

        Returns:
            (dict) -- [dictionnary holding description of object]
        """
        if not attrs or type(attrs) is not list:
            return self.__dict__
        if isinstance(attrs, list) and ([isinstance(n, str)] for n in attrs):
            return {item: getattr(self, item) for item in attrs if
                    hasattr(self, item)}

    def reload_from_json(self, json):
        """method that replaces all attributes of Student instance

        Arguments:
            json{[json]} -- [dictionary]
        """
        for attr in json.items():
            self.__dict__[attr] = json[attr]
