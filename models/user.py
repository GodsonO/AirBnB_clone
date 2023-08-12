#!/usr/bin/python3
"""Creates auser"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class that inherits from BaseModel
    attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
