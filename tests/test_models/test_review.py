#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from unittest.mock import patch
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def setUp(self):
        self.review = Review()

    def test_no_args_instantiates(self):
        self.assertIsInstance(self.review, Review)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(self.review, models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertIsInstance(self.review.id, str)

    # Add other instantiation tests...


class TestReviewSave(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

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
        self.review = Review()

    def test_one_save(self):
        first_updated_at = self.review.updated_at
        with patch('time.sleep'):
            self.review.save()
        self.assertLess(first_updated_at, self.review.updated_at)

    # Add other save tests...


class TestReviewToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def setUp(self):
        self.review = Review()

    def test_to_dict_type(self):
        self.assertIsInstance(self.review.to_dict(), dict)

    # Add other to_dict tests...


if __name__ == "__main__":
    unittest.main()

