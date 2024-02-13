#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def setUp(self):
        self.console = HBNBCommand()

    def test_help_messages(self):
        help_messages = {
            "quit": "Quit command to exit the program.",
            "create": ("Usage: create <class>\n        "
                       "Create a new class instance and print its id."),
            "EOF": "EOF signal to exit the program.",
            "show": ("Usage: show <class> <id> or <class>.show(<id>)\n        "
                     "Display the string representation of a class instance of"
                     " a given id."),
"destroy": ("Usage: destroy <class> <id> or <class>.destroy(<id>)\n"

                        "Delete a class instance of a given id."),
"all": ("Usage: all or all <class> or <class>.all()\n"
"Display string representations of all instances of a given class"                    
".\n        If no class is specified, displays all instantiated "
                    "objects."),
            "count": ("Usage: count <class> or <class>.count()\n        "
                      "Retrieve the number of instances of a given class.")
        }
        with patch("sys.stdout", new=StringIO()) as output:
            for command, message in help_messages.items():
                with self.subTest(command=command):
                    self.assertFalse(self.console.onecmd(f"help {command}"))
self.assertEqual(message, output.getvalue().strip())
def test_help(self):
    expected_output = ("Documented commands (type help <topic>):\n"
"==========================   ==============\n"                       
"EOF  all  count  create  destroy  help  quit  show  update")
    with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("help"))
        self.assertEqual(expected_output, output.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_create(unittest.TestCase):
    """Unittests for testing create from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        cls.backup_filename = "tmp.json"
        cls.backup_objects = FileStorage.__objects.copy()
        try:
            os.rename("file.json", cls.backup_filename)
        except FileNotFoundError:
            pass
        FileStorage.__objects.clear()

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename(cls.backup_filename, "file.json")
        except FileNotFoundError:
            pass
        FileStorage.__objects = cls.backup_objects

    def test_create_missing_class(self):
        expected_output = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_create_invalid_class(self):
        expected_output = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_create_invalid_syntax(self):
        expected_output = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_create_object(self):
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
                self.assertLess(0, len(output.getvalue().strip()))
                test_key = f"{class_name}.{output.getvalue().strip()}"
                self.assertIn(test_key, storage.all().keys())

		class TestHBNBCommand_show(unittest.TestCase):
    """Unittests for testing show from the HBNB command interpreter"""

    @classmethod
    def setUpClass(cls):
        cls.backup_filename = "tmp.json"
        cls.backup_objects = FileStorage.__objects.copy()
        try:
            os.rename("file.json", cls.backup_filename)
        except FileNotFoundError:
            pass
        FileStorage.__objects.clear()

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename(cls.backup_filename, "file.json")
        except FileNotFoundError:
            pass
        FileStorage.__objects = cls.backup_objects

    def test_show_missing_class(self):
        expected_output = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(expected_output, output.getvalue().strip())
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_invalid_class(self):
        expected_output = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(expected_output, output.getvalue().strip())
            self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_missing_id(self):
        expected_output = "** instance id missing **"
        commands = [
            "show BaseModel", "show User", "show State", "show City",
            "show Amenity", "show Place", "show Review",
            "BaseModel.show()", "User.show()", "State.show()", "City.show()",
            "Amenity.show()", "Place.show()", "Review.show()"
        ]
        with patch("sys.stdout", new=StringIO()) as output:
            for command in commands:
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_no_instance_found(self):
        expected_output = "** no instance found **"
        commands = [
            "show BaseModel 1", "show User 1", "show State 1", "show City 1",
            "show Amenity 1", "show Place 1", "show Review 1",
            "BaseModel.show(1)", "User.show(1)", "State.show(1)", "City.show(1)",
            "Amenity.show(1)", "Place.show(1)", "Review.show(1)"
        ]
        with patch("sys.stdout", new=StringIO()) as output:
            for command in commands:
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_objects(self):
        commands = [
            "BaseModel", "User", "State", "Place", "City", "Amenity", "Review"
        ]
        with patch("sys.stdout", new=StringIO()) as output:
            for command in commands:
                self.assertFalse(HBNBCommand().onecmd(f"create {command}"))
                test_id = output.getvalue().strip()
                obj = storage.all()[f"{command}.{test_id}"]
                self.assertFalse(HBNBCommand().onecmd(f"show {command} {test_id}"))
                self.assertEqual(obj.__str__(), output.getvalue().strip())
		
		class TestHBNBCommand_show_objects_space_notation(unittest.TestCase):
    """Unittests for testing show from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        cls.class_names = ["BaseModel", "User", "State", "Place", "City", "Amenity", "Review"]
        cls.commands = [(cls.class_names[i], f"{cls.class_names[i]}.show") for i in range(len(cls.class_names))]

    @patch("sys.stdout", new_callable=StringIO)
    def test_show_objects(self, mock_stdout):
        for class_name, command in self.commands:
            with self.subTest(class_name=class_name, command=command):
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
                test_id = mock_stdout.getvalue().strip()
                obj = storage.all()[f"{class_name}.{test_id}"]
                self.assertFalse(HBNBCommand().onecmd(f"{command}({test_id})"))
                self.assertEqual(obj.__str__(), mock_stdout.getvalue().strip())


class TestHBNBCommand_destroy(unittest.TestCase):
    """Unittests for testing destroy from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        storage.reload()
	
	class TestHBNBCommand_destroy(unittest.TestCase):
    """Unittests for testing destroy from the HBNB command interpreter."""

    def test_destroy_missing_class(self):
        """Test destroy command with missing class name."""
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_class(self):
        """Test destroy command with invalid class name."""
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_id_missing(self):
        """Test destroy command with missing instance ID."""
        correct = "** instance id missing **"
        for class_name in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"destroy {class_name}"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"{class_name}.destroy()"))
                self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_id(self):
        """Test destroy command with invalid instance ID."""
        correct = "** no instance found **"
        for class_name in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"destroy {class_name} 1"))
                self.assertEqual(correct, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"{class_name}.destroy(1)"))
                self.assertEqual(correct, output.getvalue().strip())

		class TestHBNBCommand_destroy(unittest.TestCase):
    """Unittests for testing destroy from the HBNB command interpreter."""

    def test_destroy_invalid_id_dot_notation(self):
        """Test destroy command with invalid instance ID in dot notation."""
        correct = "** no instance found **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                command = f"{class_name}.destroy(1)"
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_objects(self):
        """Test destroy command with valid instance IDs."""
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()[f"{class_name}.{testID}"]
                command = f"{class_name}.destroy({testID})"
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
	
	class TestHBNBCommand_all(unittest.TestCase):
    """Unittests for testing all of the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_all_invalid_class(self):
        """Test 'all' command with invalid class."""
        correct = "** class doesn't exist **"
        for command in ["all MyModel", "MyModel.all()"]:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(correct, output.getvalue().strip())

    def test_all_objects(self):
        """Test 'all' command with valid classes."""
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("all"))
                self.assertIn(class_name, output.getvalue().strip())

    def test_all_single_object(self):
        """Test 'all' command for single object."""
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"all {class_name}"))
                self.assertIn(class_name, output.getvalue().strip())

    def test_all_objects_dot_notation(self):
        """Test 'all' command with dot notation."""
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"{class_name}.all()"))
                self.assertIn(class_name, output.getvalue().strip())


class TestHBNBCommand_update(unittest.TestCase):
    """Unittests for testing update from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_update_missing_class(self):
        """Test 'update' command with missing class."""
        correct = "** class name missing **"
        for command in ["update", ".update()"]:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_class(self):
        """Test 'update' command with invalid class."""
        correct = "** class doesn't exist **"
        for command in ["update MyModel", "MyModel.update()"]:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_id(self):
        """Test 'update' command with missing ID."""
        correct = "** instance id missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"update {class_name}"))
                self.assertEqual(correct, output.getvalue().strip())

	class TestHBNBCommand_update(unittest.TestCase):
    """Unittests for testing update from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_update_missing_id(self):
        """Test 'update' command with missing ID."""
        correct = "** instance id missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"{class_name}.update()"))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_id(self):
        """Test 'update' command with invalid ID."""
        correct = "** no instance found **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"update {class_name} 1"))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_name(self):
        """Test 'update' command with missing attribute name."""
        correct = "** attribute name missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
                test_id = output.getvalue().strip()
                test_cmd = f"update {class_name} {test_id}"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(test_cmd))
                self.assertEqual(correct, output.getvalue().strip())

	class TestHBNBCommand_update(unittest.TestCase):
    """Unittests for testing update from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_update_missing_attr_name(self):
        """Test 'update' command with missing attribute name."""
        correct = "** attribute name missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
                test_id = output.getvalue().strip()
                test_cmd = f"{class_name}.update({{}})".format(test_id)
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(test_cmd))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_value(self):
        """Test 'update' command with missing attribute value."""
        correct = "** value missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {class_name}")
                test_id = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                test_cmd = f"update {class_name} {{}} attr_name".format(test_id)
                self.assertFalse(HBNBCommand().onecmd(test_cmd))
                self.assertEqual(correct, output.getvalue().strip())
	class TestHBNBCommand_update(unittest.TestCase):
    """Unittests for testing update from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_update_missing_attr_value(self):
        """Test 'update' command with missing attribute value."""
        correct = "** value missing **"
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {class_name}")
                test_id = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                test_cmd = f"{class_name}.update({{}}, 'attr_name')".format(test_id)
                self.assertFalse(HBNBCommand().onecmd(test_cmd))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_valid_attr_string(self):
        """Test 'update' command with valid string attribute."""
        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {class_name}")
                test_id = output.getvalue().strip()
            test_cmd = f"update {class_name} {test_id} attr_name 'attr_value'"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(test_cmd))
                test_dict = storage.all()[f"{class_name}.{test_id}"].__dict__
                self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_attr_int(self):
        """Test 'update' command with valid integer attribute."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()
        test_cmd = f"update Place {test_id} max_guest 98"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            test_dict = storage.all()[f"Place.{test_id}"].__dict__
            self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_attr_float(self):
        """Test 'update' command with valid float attribute."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()
        test_cmd = f"update Place {test_id} latitude 7.2"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_cmd))
            test_dict = storage.all()[f"Place.{test_id}"].__dict__
            self.assertEqual(7.2, test_dict["latitude"])
	class TestHBNBCommand_update(unittest.TestCase):
    """Unittests for testing update from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_update_valid_float_attr_dot_notation(self):
        """Test 'update' command with valid float attribute using dot notation."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            tId = output.getvalue().strip()
        test_cmd = f"Place.update({tId}, latitude, 7.2)"
        self.assertFalse(HBNBCommand().onecmd(test_cmd))
        test_dict = storage.all()[f"Place.{tId}"].__dict__
        self.assertEqual(7.2, test_dict["latitude"])

    def test_update_valid_dictionary(self):
        """Test 'update' command with valid dictionary attribute."""
        classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {class_name}")
                testId = output.getvalue().strip()
            test_cmd = f"update {class_name} {testId} "
            test_cmd += "{'attr_name': 'attr_value'}"
            HBNBCommand().onecmd(test_cmd)
            test_dict = storage.all()[f"{class_name}.{testId}"].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_with_int_space_notation(self):
        """Test 'update' command with valid dictionary attribute containing an int."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        test_cmd = f"update Place {testId} "
        test_cmd += "{'max_guest': 98})"
        HBNBCommand().onecmd(test_cmd)
        test_dict = storage.all()[f"Place.{testId}"].__dict__
        self.assertEqual(98, test_dict["max_guest"])

	class TestHBNBCommand_update(unittest.TestCase):
    """Unittests for testing update from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_update_valid_dictionary_with_int_dot_notation(self):
        """Test 'update' command with valid dictionary attribute containing an int using dot notation."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        test_cmd = f"Place.update({testId}, "
        test_cmd += "{'max_guest': 98})"
        HBNBCommand().onecmd(test_cmd)
        test_dict = storage.all()[f"Place.{testId}"].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_dictionary_with_float_space_notation(self):
        """Test 'update' command with valid dictionary attribute containing a float using space notation."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        test_cmd = f"update Place {testId} "
        test_cmd += "{'latitude': 9.8})"
        HBNBCommand().onecmd(test_cmd)
        test_dict = storage.all()[f"Place.{testId}"].__dict__
        self.assertEqual(9.8, test_dict["latitude"])

    def test_update_valid_dictionary_with_float_dot_notation(self):
        """Test 'update' command with valid dictionary attribute containing a float using dot notation."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        test_cmd = f"Place.update({testId}, "
        test_cmd += "{'latitude': 9.8})"
        HBNBCommand().onecmd(test_cmd)
        test_dict = storage.all()[f"Place.{testId}"].__dict__
        self.assertEqual(9.8, test_dict["latitude"])


class TestHBNBCommand_count(unittest.TestCase):
    """Unittests for testing count method of HBNB comand interpreter."""

    @classmethod
    def setUp(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDown(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_count_invalid_class(self):
        """Test count method with an invalid class."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
            self.assertEqual("0", output.getvalue().strip())

    def test_count_object(self):
        """Test count method with a valid class."""
        classes = ["BaseModel", "User", "State", "Place", "City", "Amenity", "Review"]
        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {class_name}"))
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"{class_name}.count()"))
                self.assertEqual("1", output.getvalue().strip())



if __name__ == "__main__":
    unittest.main()

