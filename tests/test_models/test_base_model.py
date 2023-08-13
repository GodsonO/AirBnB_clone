#!/usr/bin/python3

import unittest
import pep8
from os import path, remove
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        Testing the Base Model class
    """

    @classmethod
    def setup(self):
        """Setup the class"""
        pass

    @classmethod
    def tearDown(self):
        """Cleanup each class"""
        try:
            if path.exists("file.json"):
                remove('file.json')
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """Test if pep8 style is followed"""
        check_style = pep8.StyleGuide(quiet=True)
        pep = check_style.check_files(['models/base_model.py'])
        self.assertEqual(pep.total_errors, 0, 'fix pep8')

    def test_function(self):
        """Test for all the functions in the base model class"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__)
        self.assertIsNotNone(BaseModel.save.__doc__)


if __name__ == "__main__":
    unittest.main()
