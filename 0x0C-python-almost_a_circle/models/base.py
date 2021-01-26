#!/usr/bin/python3
""" Base definition """
from os import path
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base initialization

        Arguments:
            id ([int], optional): [the id]. Defaults to None
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json string representation

        Args:
            list_dictionaries ([list of dicts]): list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representatios to a file, definition

        Args:
            list_objs ([list of objects]): lifs of objects
        """
        My_list = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as MyFile:
            if list_objs is None:
                MyFile.write(Base.to_jason_string("[]"))
            for item in list_objs:
                My_list.append(item.to_dictionary())
            MyFile.write(Base.to_json_string(My_list))

    @staticmethod
    def from_json_string(json_string):
        """ from JSON to string definition

        Args:
            json_string ([json_string]): json string
        """
        if json_string is None or json_string is []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ class method creation

        returns:
        [instance of obj]: instance of all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
            dummy_instance.update(**dictionary)
        if cls.__name__ == "Square":
            dummy_instance = cls(1)
            dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ load from file method

        returns:
            [list]: list of instances
        """
        filename = cls.__name__ + "json"
        if not path.exists(filename):
            return []
        with open(filename, mode="r") as MyFile:
            My_list = cls.from_json_string(MyFile.read())
            list_of_instances = [cls.create(**attrs) for attrs in My_list]
            return list_of_instances
