#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
<<<<<<< HEAD
        new = self.value()
        self.assertTrue(isinstance(new.first_name, str)
                        or new.first_name is None)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertTrue(isinstance(new.last_name, str)
                        or new.last_name is None)
=======
        new = self.value(email="test@example.com", password="test")
        self.assertTrue(isinstance(new.first_name, str) or new.first_name is None)

    def test_last_name(self):
        """ """
        new = self.value(email="test@example.com", password="test")
        self.assertTrue(isinstance(new.last_name, str) or new.last_name is None)
>>>>>>> 2541da006e16d2f20d332a7a7d907558da833e01

    def test_email(self):
        """ """
        new = self.value(email="test@example.com", password="test")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value(email="test@example.com", password="test")
        self.assertEqual(type(new.password), str)
