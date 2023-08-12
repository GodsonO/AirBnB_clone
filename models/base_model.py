#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
import uuid
from datetime import datetime


class BaseModel:
    """The BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key-value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, v in kwargs.items():
                if key == "created_at":
                    self.__dict__[key] = datetime.strptime(
                        v, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        v, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a str representation of the BaseModel instance."""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
