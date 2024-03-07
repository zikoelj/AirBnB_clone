#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """to Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, file)

    def reload(self):
         """
         that deserializes the data in our JSON file back
         to the dictionary __objects
         """
         try:
             with open(FileStorage.__file_path, encoding="utf-8") as file:
                 desr_file = json.load(file)
                 for v in desr_file.values():
                     cls_name = v["__class__"]
                     if isinstance(cls_name, str) and type(eval(cls_name)) == type:
                         self.new(eval(cls_name)(**v))
         except FileNotFoundError:
             pass

