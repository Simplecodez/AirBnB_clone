#!/usr/bin/python3
"""
A Base model class for the python AirBnB clone
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A base model class that defines all attributes and methods for other objects and classes to inherit from

    Today 8/3/2023 - The main change is in the '__init__' method. Now if Now, if the constructor is called with a dictionary (kwargs), the method loops through each key-value pair in the dictionary and sets the corresponding attribute of the object using the setattr function."""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                """8/3/2023 - If the key is "created_at" or "updated_at", the value is converted from a string to a datetime object using the strptime function, which takes a string and a format specifier and returns a datetime object."""
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                """8/3/2023 - If the dictionary does not contain an "id" key, a new unique identifier is generated. Finally, the created_at and updated_at attributes are set to the current time if they are not provided in the dictionary."""
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
