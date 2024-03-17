#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def to_dict(self):
        """
        Return a dictionary representation of the User instance.
        """
        user_dict = super().to_dict()
        user_dict['__class__'] = self.__class__.__name__
        return user_dict

    def all(cls):
        """Retourne toutes les instances de la classe User."""
        return storage.all(cls)

    def count():
        """Retrieves the number of instances of the class."""
        return len(storage.all(self))
