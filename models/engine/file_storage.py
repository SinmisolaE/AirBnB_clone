#!/usr/bin/python3
""" Defines a class FileStorage """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review improt Review


class FileStorage:
    """ Serializes instances to JSON file and
        Deserializes JSON file to instances
    """

    __file_path = ""
    __objects = {}

    def all(self):
        """ Returns the dictionary __object """
        return FileStorage.__objects

    def new(self):
        """ sets in __objects the obj with key <obj class name>.id """
        name = type(obj).__name__
        FileStorage.__objects["{}.{}".format(name, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        file = FileStorage.__file_path
        dict = FileStorage.__objects
        objdict = {obj: dict[obj].to_dict() for obj in dict.keys()}
        with open(file, 'w', encoding='UTF8') as f:
            json.dumps(objdict, f)

    def reload(self):
        """ Deserializes JSON file to __objects """
        file = FileStorage.__file_path
        try:
            with open(file, encoding='UTF8') as f:
                objects = json.loads(file)
                for obj in objects.values():
                    cls_name = obj[__class__]
                    del obj[__class__]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return;
