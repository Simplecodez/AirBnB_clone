#!/usr/bin/python3
"""
A Base model class for the python AirBnB clone
"""

from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """
    A base model class that defines all attributes and methods for other objects and classes to inherit from"""

    def __init__(self, *args, **kwargs):
        """Constructor for the BaseModel Class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            self.id = kwargs.get("id", str(uuid.uuid4()))
            self.created_at = kwargs.get("created_at", datetime.now())
            self.updated_at = kwargs.get("updated_at", datetime.now())
        else:
            self.id = str(uuid.uuid4())
            #self.created_at = datetime.datetime.now()
            #self.created_at = datetime.datetime.now() will fail because of the method you used to import the datetime module. That is why I changed tweaked it a little
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        result_dict = self.__dict__.copy()
        result_dict["__class__"] = type(self).__name__
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        return result_dict
