#!/usr/bin/python3

'''
A module that contains the test cases for the class BaseModel
'''
import unittest
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_instantiation(self):
        """Test that the BaseModel class can be instantiated with the correct attributes."""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_method(self):
        """Test that the save() method correctly updates the updated_at attribute."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict_method(self):
        """Test that the to_dict() method returns a dictionary with the correct keys and values."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_init_with_dict(self):
        """Test that passing a dictionary to the __init__() method correctly sets the instance attributes."""
        model_dict = {
            "id": uuid4(),
            "created_at": datetime.isoformat(),
            "updated_at": datetime.isoformat(),
        }
    
        model = BaseModel(**model_dict)
        self.assertEqual(model.id, str(uuid4()))
        self.assertEqual(model.created_at, datetime.isoformat())
