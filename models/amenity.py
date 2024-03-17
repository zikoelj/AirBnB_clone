#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity."""

    name = ""

    def count():
        """Retrieves the number of instances of the class."""
        return len(storage.all(self))
