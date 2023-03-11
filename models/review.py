#!/usr/bin/python3
"""
The class Review should inherit BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    All attrbutes are empty
    """
    place_id = ""
    user_id = ""
    text = ""
