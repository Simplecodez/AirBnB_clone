#!/usr/bin/python3
""" 0x00. AirBnB clone - The console """
import json
from os import path


class FileStorage:
    """ Class meant to manage JSON file storage for `BaseModel` and its child
        classes.

        Attributes:
        __file_path (str): default path to save JSON serializations to file
        __objects (dict): dict of items with `BaseModel` and its child classes
            as values, and '<object class name>.<object.id>' as keys

        Project tasks:
        5. Store first object

    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """Returns the dictionary __objects.
           Returns:
               __objects (dict): dict of items with `BaseModel` and its child
                classes as values, and '<object class name>.<object.id>' as
                    keys

            Project tasks:
                5. Store first object

        """
        return self.__objects

    def new(self, obj):
        """Sets a new object as value in __objects with key
           '<object class name>.<object.id>'

           Args:
           obj (BaseModel or child): BaseModel-derived object to be added to
           __objects

           Project tasks:
           5. Store first object

        """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
           Project tasks:
           5. Store first object

        """
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(json_dict))

    def reload(self):
        """Deserializes the JSON file at __file_path into  __objects, if it
           exists; otherwise, no exception is raised.

           Project tasks:
           5. Store first object

        """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        all_class = {
            "BaseModel": BaseModel,
            "User": User,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State
        }

        if path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                if content is not None and content != '':
                    json_dict = json.loads(content)
                    for key, value in json_dict.items():
                        class_name = key.split('.')[0]
                        self.__objects[key] = all_class[class_name](**value)

        else:
            pass
