#!/usr/bin/python3
""" """
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """ """

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        """ """
        console = HBNBCommand()
        with self.assertRaises(SystemExit):
            console.do_quit(None)
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_quit(self, mock_stdout):
        """ """
        console = HBNBCommand()
        console.help_quit()
        self.assertEqual(mock_stdout.getvalue(),
                         "Exits the program with formatting\n\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        console = HBNBCommand()
        with self.assertRaises(SystemExit):
            console.do_EOF(None)
        self.assertEqual(mock_stdout.getvalue(), "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_EOF(self, mock_stdout):
        console = HBNBCommand()
        console.help_EOF()
        self.assertEqual(mock_stdout.getvalue(),
                         "Exits the program without formatting\n\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        console = HBNBCommand()
        console.emptyline()
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('builtins.print')
    def test_do_create(self, mock_print):
        console = HBNBCommand()
        console.classes['TestModel'] = lambda: None
        console.do_create("TestModel")
        mock_print.assert_called()

    @patch('builtins.print')
    def test_help_create(self, mock_print):
        console = HBNBCommand()
        console.help_create()
        mock_print.assert_called()

    @patch('builtins.print')
    def test_do_show(self, mock_print):
        console = HBNBCommand()
        console.classes['TestModel'] = lambda: None
        console.do_show("TestModel 1234")
        mock_print.assert_called()

    @patch('builtins.print')
    def test_help_show(self, mock_print):
        console = HBNBCommand()
        console.help_show()
        mock_print.assert_called()

    @patch('builtins.print')
    def test_do_destroy(self, mock_print):
        console = HBNBCommand()
        console.classes['TestModel'] = lambda: None
        console.do_destroy("TestModel 1234")
        mock_print.assert_called()

    @patch('builtins.print')
    def test_help_destroy(self, mock_print):
        console = HBNBCommand()
        console.help_destroy()
        mock_print.assert_called()

    @patch('builtins.print')
    def test_do_all(self, mock_print):
        console = HBNBCommand()
        console.do_all("TestModel")
        mock_print.assert_called()

    @patch('builtins.print')
    def test_help_all(self, mock_print):
        console = HBNBCommand()
        console.help_all()
        mock_print.assert_called()

    @patch('builtins.print')
    def test_do_count(self, mock_print):
        console = HBNBCommand()
        console.do_count("TestModel")
        mock_print.assert_called()

    @patch('builtins.print')
    def test_help_count(self, mock_print):
        console = HBNBCommand()
        console.help_count()
        mock_print.assert_called()

    @patch('builtins.print')
    def test_do_update(self, mock_print):
        console = HBNBCommand()
        console.classes['TestModel'] = lambda: None
        console.do_update("TestModel 1234 name John")
        mock_print.assert_called()

    @patch('builtins.print')
    def test_help_update(self, mock_print):
        console = HBNBCommand()
        console.help_update()
        mock_print.assert_called()


if __name__ == '__main__':
    unittest.main()
