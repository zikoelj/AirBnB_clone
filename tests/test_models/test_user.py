#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up testing environment"""
        self.user = User()

    def tearDown(self):
        """Clean up after each test"""
        del self.user

    def test_attributes(self):
        """Test default attribute values"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str(self):
        """Test __str__ method"""
        user_str = str(self.user)
        self.assertIn("[User]", user_str)
        self.assertIn("'id':", user_str)
        self.assertIn("'created_at':", user_str)
        self.assertIn("'updated_at':", user_str)

    def test_to_dict(self):
        """Test to_dict method"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], "User")
        self.assertEqual(user_dict["email"], "")
        self.assertEqual(user_dict["password"], "")
        self.assertEqual(user_dict["first_name"], "")
        self.assertEqual(user_dict["last_name"], "")

    def test_save(self):
        """Test save method"""
        prev_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(prev_updated_at, self.user.updated_at)


if __name__ == "__main__":
    unittest.main()
