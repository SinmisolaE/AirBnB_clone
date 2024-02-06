#!/usr/bin/python3
""" Defines class BaseModel """

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ Defines all common attributes/methods
        for other classes """

    def __init__(self, *args, **kwargs):
        """ Initializes attributes 
            addition *args and **kwargs should be used
            *args won't be used
        """

        if len(kwargs) != 0:
            for key, val in kwargs.iteritems():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.fromisoformat(val)
                    self.__dict__[key] = val
        else:
            self.id = str(uuid4())
            self.created_at = date_time.today()
            self.updated_at = date_time.today()

    def __str__(self):
        """ Returns printable representation """
        name = type(self).__name__
        return ("[{}] ({}) {}".format(name, self.id, self.__dict__))

    def save(self):
        """ Updates the attribute (updated_at) with current datetime"""
        self.updated_at = date_time.today()
        storage.save()

    def to_dict(self):
        """ returns dictionary containing all keys/values of __dict__
            __class__ must be added with the class name of object
            created_at and updated_at must be converted to string in ISO format
        """
        dict = self.__dict__.copy()
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        dict["__class__"] = type(self).__name__
        return dict
