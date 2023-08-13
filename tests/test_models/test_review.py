#!/usr/bin/python3
"""Unittest for review.py"""
import unittest
from models.review import Review
from models.base_model import BaseModel
import os


class TestPlace(unittest.TestCase):
    """Class to test review.py"""

    def setUp(self):
        """Sets up the testing environment"""

        self.r1 = Review()
        self.r2 = Review()
        self.r2.text = "Terrible"

    def tearDown(self):
        """Tears down the testing environment"""

        del self.r1
        del self.r2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_non_existant_instance(self):
        """Checks for a non-existant instance"""

        self.r3 = Review()
        self.assertIsInstance(self.r3, Review)

    def test_inheritence(self):
        """Checks to make sure Review inherits from BaseModel"""

        self.assertTrue(issubclass(Review, BaseModel))

    def test_checks_attributes(self):
        """Checks for class specific attributes"""

        self.assertTrue(hasattr(Review(), "place_id"))
        self.assertTrue(hasattr(Review(), "user_id"))
        self.assertTrue(hasattr(Review(), "text"))

    def test_new_instances(self):
        """Checks that new instances were created"""

        self.assertTrue(self.r1)
        self.assertTrue(self.r2)

    def test_new_instances_attribute_creation(self):
        """Checks that new instances have designated attributes"""

        self.assertIn("text", self.r2.__dict__)
        self.assertEqual(self.r2.text, "Terrible")

if __name__ == "__main__":
    unittest.main()
