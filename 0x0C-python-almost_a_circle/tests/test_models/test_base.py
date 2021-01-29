#!/usr/bin/python3
""" test_base """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ class to test Base

    Args:
        unittest ([unittest]): [unit testing framework]
    """

    def test_base_zero_args(self):
        """ test args for our base """
        B = Base(1)
        self.assertEqual(B.id, 1)

    def test_base_negative(self):
        """ test negative """
        B = Base(-1)
        self.assertEqual(B.id, -1)

    def test_base_int(self):
        """ test int """
        B = Base(53)
        self.assertEqual(B.id, 53)

    def test_base_string(self):
        """ test str """
        B = Base("fares")
        self.assertEqual(B.id, "fares")

    def test_base_none(self):
        """ test None """
        B = Base(None)
        self.assertEqual(B.id, 1)

    def test_base_float(self):
        """ test float """
        B = Base(3.14)
        self.assertEqual(B.id, 3.14)

    def test_base_list(self):
        """ test list """
        B = Base([1, 2, 3, 4])
        self.assertEqual(B.id, [1, 2, 3, 4])

    def test_base_dict(self):
        """ test dict """
        B = Base({"Holberton": "School"})
        self.assertEqual(B.id, {"Holberton": "School"})

if __name__ == '__main__':
    unittest.main()
