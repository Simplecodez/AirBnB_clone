#!/usr/bin/python3
"""
A Base model class for the python AirBnB clone
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A base model class that defines all attributes and methods for other objects and classes to inherit from"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        result_dict = self.__dict__.copy()
        result_dict["__class__"] = type(self).__name__
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        return result_dict

