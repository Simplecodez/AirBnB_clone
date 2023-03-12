#!/usr/bin/python3
""" 0x00. AirBnB clone - The console """
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods for `BaseModel` and its subclasses.

        Use of kwargs is currently very brittle and assumes no use of *args,
        and either empty **kwargs, or a dictionary that contains a key for every
        instance attribute named in `__init__`, and corresponding values of the
        correct type and formatting.

        Attributes:
            id (str): a unique UUID that is assigned when an instance is created
            created_at (datetime.datetime): the current datetime when an instance
                is created
            updated_at (datetime.datetime): the current datetime when an instance
                is created, but updated everytime object is changed

    """
    def __init__(self, *args, **kwargs):
        """`BaseModel` class constructor.

                Project tasks:
                    3. BaseModel
                    4. Create BaseModel from dictionary

        """
        if kwargs:
            iso_fmt = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(value, iso_fmt)
                    else:
                        self.__dict__[key] = value

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns the string representation of BaseModel.

                Returns:
                     '[<class name>] (<self.id>) <self.__dict__>'

                Project tasks:
                    3. BaseModel
        """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime. Save updates to JSON
                serialization.

                Project tasks:
                    3. BaseModel
                    5. Store first object

        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
                of the instance, plus `__class__`, `created-at`, and `updated_at`.

                Project tasks:
                    3. BaseModel

        """
        myresult = self.__dict__.copy()
        myresult["__class__"] = self.__class__.__name__
        myresult["created_at"] = self.created_at.isoformat()
        myresult["updated_at"] = self.updated_at.isoformat()

        return myresult
