#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    TestMaxInteger class

    unittest {[builtin]} -- [built in to unit test]
    """
    def test_empty_list(self):
        """
        test if list is empty
        """
        self.assertEqual(max_integer([]), None)

    def test_max_begin(self):
        """
        test if max int is at the begining
        """
        self.assertEqual(max_integer([5, 3, 4, 1]), 5)

    def test_max_mid(self):
        """
        test if max int is at the middle
        """
        self.assertEqual(max_integer([5, 3, 8, 4, 1]), 8)

    def test_max_end(self):
        """
        test if max int is at the end
        """
        self.assertEqual(max_integer([5, 3, 4, 8]), 8)

    def text_max_negative(self):
        """
        test if max negative is max
        """
        self.assertEqual(max_integer([-5, -3, -4, -8]), -3)

    def test_float_int(self):
        """ test max through float and int
        """
        self.assertEqual(max_integer([-5, 4.5, 4, 9.66]), 9.66)

    def test_max_str(self):
        """
        test max through a string
        """
        self.assertEqual(max_integer("abcdef"), "f")

    def test_mixed_int_str(self):
        """
        test mised types in list
        """
        with self.assertRaises(TypeError):
            max_integer(["hol", "berton", 7])

if __name__ == '__main__':
    unittest.main()
