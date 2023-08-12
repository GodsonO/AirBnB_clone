#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


class FileStorage:
    """Represent a storage engine."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key"""
        k = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(k, obj.id)] = obj

    def save(self):
        """
            Serialize __objects to the JSON file
            (path:__file_path.)
        """
        o_dict = FileStorage.__objects
        with open(FileStorage.__file_path, "w") as f:
            object_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
            json.dump(object_dict, f)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """
            Deserialize the JSON file __file_path to __objects,
            (only if JSON file exists)
        """
        try:
            with open(FileStorage.__file_path) as f:
                object_dict = json.load(f)
                for obj in object_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
