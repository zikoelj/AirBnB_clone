#!/usr/bin/pythpn3
"""
This module to test FileStorage class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """
    This class to test FileStorage class
    """
    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down test environment."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test all method."""
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(len(self.storage.all()), 0)

    def test_new(self):
        """Test new method."""
        obj = BaseModel()
        self.storage.new(obj)
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(obj_key, self.storage.all().keys())

    def test_save_reload(self):
        """Test save and reload methods."""
        obj = BaseModel()
        obj.save()
        self.storage.reload()
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(obj_key, self.storage.all().keys())

if __name__ == "__main__":
    unittest.main()
