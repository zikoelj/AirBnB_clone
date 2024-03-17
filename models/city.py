#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city."""

    state_id = ""
    name = ""

    def count():
        """Retrieves the number of instances of the class."""
        return len(storage.all(self))
