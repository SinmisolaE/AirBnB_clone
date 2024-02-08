#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from unittest.mock import patch
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def setUp(self):
        self.place = Place()

    def test_no_args_instantiates(self):
        self.assertIsInstance(self.place, Place)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(self.place, models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertIsInstance(self.place.id, str)

    # Add other instantiation tests...


class TestPlaceSave(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

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
        self.place = Place()

    def test_one_save(self):
        first_updated_at = self.place.updated_at
        with patch('time.sleep'):
            self.place.save()
        self.assertLess(first_updated_at, self.place.updated_at)

    # Add other save tests...


class TestPlaceToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def setUp(self):
        self.place = Place()

    def test_to_dict_type(self):
        self.assertIsInstance(self.place.to_dict(), dict)

    # Add other to_dict tests...


if __name__ == "__main__":
    unittest.main()

