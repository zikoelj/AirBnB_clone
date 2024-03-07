#!/usr/bin/python3
"""Defines the BaseModel class."""

from uuid import uuid4
from datetime import datetime


class BaseModel:
        """Defines the base model class."""
            
        def __init__(self, *args, **kwargs):
            """Initializes a new instance of BaseModel."""
            if kwargs:
                for key, value in kwargs.items():
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    if key != '__class__':
                        setattr(self, key, value)
            else:
                self.id = str(uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

        def __str__(self):
            """Returns a string representation of the BaseModel instance."""
            return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

        def save(self):
            """Updates the updated_at attribute with the current datetime."""
            self.updated_at = datetime.now()
        
        def to_dict(self):
            """Returns a dictionary representation of the BaseModel instance."""
            obj_dict = self.__dict__.copy()
            obj_dict['__class__'] = type(self).__name__
            obj_dict['created_at'] = self.created_at.isoformat()
            obj_dict['updated_at'] = self.updated_at.isoformat()
            return obj_dict

# Testing the BaseModel class
if __name__ == "__main__":
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        print(my_model)
        my_model.save()
        print(my_model)
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
