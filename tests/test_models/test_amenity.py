"""Unittest for Amenity class"""
import unittest
import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
import os


class TestAmenity(unittest.TestCase):
    """Runs tests for Amenity class"""

    def setUp(self):
        """Sets up the testing environment"""

        self.a1 = Amenity()
        self.a2 = Amenity()
        self.a2.name = "Washer"

    def tearDown(self):
        """Breaks down the testing environment"""

        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_ids(self):
        """Checks for different IDs"""

        self.assertNotEqual(self.a1.id, self.a2.id)

    def test_names(self):
        """Checks for different names"""

        self.assertNotEqual(self.a1.name, self.a2.name)
        self.assertEqual(self.a2.name, "Washer")
        self.assertEqual(self.a1.name, "")
        self.a1.name = "Dryer"
        self.assertEqual(self.a1.name, "Dryer")
        self.assertNotEqual(self.a1.name, self.a2.name)

    def test_user_attribute(self):
        """Checks for user set attribute functionality"""

        self.assertFalse("fun_rating" in self.a1.__dict__)
        self.a1.fun_rating = 8
        self.assertEqual(self.a1.fun_rating, 8)
        self.assertTrue("fun_rating" in self.a1.__dict__)
        self.assertFalse("fun_rating" in self.a2.__dict__)

    def test_attribute_presence(self):
        """Checks to make sure attribute is present"""

        self.assertTrue(hasattr(self.a1, "name"))
        self.assertTrue(hasattr(self.a2, "name"))
        self.assertFalse(hasattr(self.a1, "number_rooms"))
        self.assertFalse(hasattr(self.a2, "number_rooms"))

    def test_attribute_type(self):
        """Checks for correct types of attributes"""

        self.assertEqual(str, type(getattr(self.a2, "name")))

    def test_created_at(self):
        """Checks for created_at attribute"""

        self.assertTrue(hasattr(self.a1, "created_at"))
        self.assertTrue(hasattr(self.a2, "created_at"))
        self.assertNotEqual(self.a2.created_at, self.a1.created_at)

    def test_updated_at(self):
        """Checks for updated_at attribute"""

        self.assertTrue(hasattr(self.a1, "updated_at"))
        self.assertTrue(hasattr(self.a2, "updated_at"))
        self.assertNotEqual(self.a2.updated_at, self.a1.updated_at)

    def test_created_updated_type(self):
        """Checks the types of created_at and updated_at"""

        self.assertTrue(datetime, type(self.a1.created_at))
        self.assertTrue(datetime, type(self.a1.updated_at))
        self.assertTrue(datetime, type(self.a2.created_at))
        self.assertTrue(datetime, type(self.a2.updated_at))

    def test_non_existant_instance(self):
        """Checks for a non-existant instance"""

        self.a3 = Amenity()
        self.assertIsInstance(self.a3, Amenity)

    def test_inheritence(self):
        """Checks to make sure Amenity inherits from BaseModel"""

        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == "__main__":
    unittest.main()
