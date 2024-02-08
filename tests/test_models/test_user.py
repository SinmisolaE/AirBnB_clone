#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUserInstantiation
    TestUserSave
    TestUserToDict
"""
import os
import models
import unittest
from datetime import datetime
from unittest.mock import patch
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def setUp(self):
        self.user = User()

    def test_no_args_instantiates(self):
        self.assertIsInstance(self.user, User)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(self.user, models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertIsInstance(self.user.id, str)

    # Add other instantiation tests...


class TestUserSave(unittest.TestCase):
    """Unittests for testing save method of the User class."""

    @classmethod
    def setUpClass(cls):
        cls.backup_file()

    @classmethod
    def tearDownClass(cls):
        cls.restore_file()

    @staticmethod
    def backup_file():
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @staticmethod
    def restore_file():
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def setUp(self):
        self.user = User()

    def test_one_save(self):
        first_updated_at = self.user.updated_at
        with patch('time.sleep'):
            self.user.save()
        self.assertLess(first_updated_at, self.user.updated_at)

    # Add other save tests...


class TestUserToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def setUp(self):
        self.user = User()

    def test_to_dict_type(self):
        self.assertIsInstance(self.user.to_dict(), dict)

    # Add other to_dict tests...


if __name__ == "__main__":
    unittest.main()

