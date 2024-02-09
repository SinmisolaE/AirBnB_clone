#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestStateInstantiation
    TestStateSave
    TestStateToDict
"""
import os
import models
import unittest
from datetime import datetime
from unittest.mock import patch
from models.state import State


class TestStateInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def setUp(self):
        self.state = State()

    def test_no_args_instantiates(self):
        self.assertIsInstance(self.state, State)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(self.state, models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertIsInstance(self.state.id, str)

    # Add other instantiation tests...


class TestStateSave(unittest.TestCase):
    """Unittests for testing save method of the State class."""

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
        self.state = State()

    def test_one_save(self):
        first_updated_at = self.state.updated_at
        with patch('time.sleep'):
            self.state.save()
        self.assertLess(first_updated_at, self.state.updated_at)

    # Add other save tests...


class TestStateToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def setUp(self):
        self.state = State()

    def test_to_dict_type(self):
        self.assertIsInstance(self.state.to_dict(), dict)

    # Add other to_dict tests...


if __name__ == "__main__":
    unittest.main()

