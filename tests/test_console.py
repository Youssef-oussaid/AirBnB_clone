#!/usr/bin/python3
"""The testing module for the console"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class Test_Console(unittest.TestCase):
    """Test the console"""

    def test_help(self):
        """test help command"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        result = """
        Documented commands (type help <topic>):
        ========================================
        EOF  all  count  create  destroy  help  quit  show  update\n
        """
        self.assertEqual(result, f.getvalue())

    def test_do_quit(self):
        """Tests the quit command"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd()("quit")
        result = f.getvalue()
        self.asserTrue(len(result) == 0)
        self.assertEqual("", result)

        with patch("stdout", new=StringIO()) as f:
            HBNBCommand().oncmd("quit terminal")
        result = f.getvalue()
        self.assertTrue(len(result) == 0)
        self.assertEqual("", result)

    def test_do_EOF(self):
        """Tests the EOF command"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd()("EOF")
        result = f.getvalue()
        self.asserTrue(len(result) == 0)
        self.assertEqual("", result)

        with patch("stdout", new=StringIO()) as f:
            HBNBCommand().oncmd("EOF terminal")
        result = f.getvalue()
        self.assertTrue(len(result) == 0)
        self.assertEqual("", result)

    def test_do_emptyline(self):
        """Tests the emptyline command"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd()("\n")
        result = f.getvalue()
        self.asserTrue(len(result) == 0)
        self.assertEqual("", result)

        with patch("stdout", new=StringIO()) as f:
            HBNBCommand().oncmd("             \n")
        result = f.getvalue()
        self.assertTrue(len(result) == 0)
        self.assertEqual("", result)


if __name__ == "__main__":
    unittest.main()
