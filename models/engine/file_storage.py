#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                FileStorage.__objects = json.load(file)
        except FileNotFoundError:
            pass
