#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorageInstantiation
    TestFileStorageMethods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorageInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_instantiation_no_args(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_is_private_str(self):
        self.assertIsInstance(FileStorage()._FileStorage__file_path, str)

    def test_objects_is_private_dict(self):
        self.assertIsInstance(FileStorage()._FileStorage__objects, dict)

    def test_storage_initializes(self):
        self.assertIsInstance(models.storage, FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

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
        except FileNotFoundError:
            pass

    @staticmethod
    def restore_file():
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def setUp(self):
        self.storage = models.storage

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            self.storage.all(None)

    def test_new(self):
        instances = [BaseModel(), User(), State(), Place(), City(), Amenity(), Review()]
        for instance in instances:
            self.storage.new(instance)
            key = "{}.{}".format(type(instance).__name__, instance.id)
            self.assertIn(key, self.storage.all())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            self.storage.new(BaseModel(), 1)

    def test_save(self):
        instances = [BaseModel(), User(), State(), Place(), City(), Amenity(), Review()]
        for instance in instances:
            self.storage.new(instance)
        self.storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
            for instance in instances:
                key = "{}.{}".format(type(instance).__name__, instance.id)
                self.assertIn(key, data)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            self.storage.save(None)

    def test_reload(self):
        instances = [BaseModel(), User(), State(), Place(), City(), Amenity(), Review()]
        for instance in instances:
            self.storage.new(instance)
        self.storage.save()
        self.storage.reload()
        for instance in instances:
            key = "{}.{}".format(type(instance).__name__, instance.id)
            self.assertIn(key, self.storage.all())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            self.storage.reload(None)


if __name__ == "__main__":
    unittest.main()

