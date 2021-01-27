#!/usr/bin/python3
""" unit testing square """
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ TestSquare

    Args:
        unittest ([unittest]): unit testting framework
    """

    def test_size_square_error(self):
        self.assertRaises(TypeError, Square, "str")
        self.assertRaises(TypeError, Square, True)
        self.assertRaises(TypeError, Square, 0.1)
        self.assertRaises(ValueError, Square, -1)

    def test_square(self):
        s1 = Square(2, 6, 3, 99)
        s2 = Square(5, 8, 8, 6)
        self.assertEqual(s1.id, 99)
        self.assertEqual(s1.x, 6)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.area(), 4)
        self.assertEqual(s2.id, 6)
        self.assertEqual(s2.x, 8)
        self.assertEqual(s2.y, 8)
        self.assertEqual(s2.width, 5)
        self.assertEqual(s2.height, 5)
        self.assertEqual(s2.size, 5)
        self.assertEqual(s2.area(), 25)

    def test_square_coordinates_error(self):
        self.assertRaises(TypeError, Square, 2, 4, "s", 7)
        self.assertRaises(TypeError, Square, 2, "s", 5, 7)
        self.assertRaises(TypeError, Square, 2, 4, True, 7)
        self.assertRaises(TypeError, Square, 2, False, 3, 7)
        self.assertRaises(TypeError, Square, 2, 4, 2.5, 7)
        self.assertRaises(TypeError, Square, 2, 1.5, 4, 7)
        self.assertRaises(ValueError, Square, 2, 4, -3, 7)
        self.assertRaises(ValueError, Square, 2, -4, 3, 7)

    def test_square_update(self):
        s1 = Square(2, 6, 3, 100)
        s1.update(99, 98, 97, 96)
        self.assertEqual(s1.id, 99)
        self.assertEqual(s1.x, 97)
        self.assertEqual(s1.y, 96)
        self.assertEqual(s1.size, 98)
        self.assertEqual(s1.area(), 9604)
        s1.update(1000, x=1, y=1)
        self.assertEqual(s1.id, 100)
        self.assertEqual(s1.x, 97)
        self.assertEqual(s1.y, 96)
        s1.update(size=1, y=1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.y, 1)

if __name__ == '__main__':
    unittest.main()
