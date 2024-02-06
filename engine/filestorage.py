#!/usr/bin/python3
""" Defines a class FileStorage """
import json


class FileStorage:
    """ Serializes instances to JSON file and
        Deserializes JSON file to instances
    """

    __file_path = ""
    __objects = {}

    def all(self):
        """ Returns the dictionary __object """
        return type(self).__objects

    def new(self):
        """ sets in __objects the obj with key <obj class name>.id """
        name = type(obj).__name__
        type(self).__objects["{}.{}".format(name, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        file = type(self).__file_path
        with open(file, 'w', encoding='UTF8') as f:
            json.dumps(type(self).__objects, f)

    def reload(self):
        """ Deserializes JSON file to __objects """
        file = type(self).__file_path
        try:
            with open(file, encoding='UTF8') as f:
                type(self).__objects = json.loads(file)
        except FileNotFoundError:
            return;
