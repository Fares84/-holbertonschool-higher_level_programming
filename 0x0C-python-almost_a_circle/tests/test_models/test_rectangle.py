#!/usr/bin/python3
""" test rectangle """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ test rectangle

    Args:
        unittest ([unittest]): unit test framework
    """
    def test_base_typeError(self):
        """ test typeError """
        self.assertRaises(TypeError, Rectangle, "Hol", "Berton")

    def test_rectangle_one_arg(self):
        """ test one argument """
        self.assertRaises(TypeError, Rectangle, 1)

    def test_width_rectangle_str(self):
        """ str error """
        self.assertRaises(TypeError, Rectangle, "s1", 2)

    def test_height_rectangle_str(self):
        """ str error """
        self.assertRaises(TypeError, Rectangle, 1, "str")

    def test_width_rectangle_float(self):
        """ float error """
        self.assertRaises(TypeError, Rectangle, 0.15, 2)

    def test_height_rectangle_str(self):
        """ float arror """
        self.assertRaises(TypeError, Rectangle, 1, 0.5)

    def test_width_rectangle_list(self):
        """ list error """
        self.assertRaises(TypeError, Rectangle, [2, 3], 1)

    def test_width_rectangle_list(self):
        """ list error """
        self.assertRaises(TypeError, Rectangle, 1, [2, 3])

    def test_width_rectangle_dict(self):
        """ list error """
        self.assertRaises(TypeError, Rectangle, {"2": 3}, 1)

    def test_height_rectangle_dict(self):
        """ list error """
        self.assertRaises(TypeError, Rectangle, 1, {"2": 3})

    def test_width_rectangle_zero(self):
        """ zero value """
        self.assertRaises(TypeError, Rectangle, None, 1)

    def test_height_rectangle_zero(self):
        """ zero value """
        self.assertRaises(TypeError, Rectangle, 1, None)

    def test_width_rectangle_negative(self):
        """ negative value """
        self.assertRaises(ValueError, Rectangle, -1, 1)

    def test_width_rectangle_negative(self):
        """ negative value """
        self.assertRaises(ValueError, Rectangle, 1, -1)

    def test_width_rectangle_bool(self):
        """ True or False """
        self.assertRaises(TypeError, Rectangle, True, 1)

    def test_height_rectangle_bool(self):
        """ True or False """
        self.assertRaises(TypeError, Rectangle, 1, True)

    def test_width_rectangle_tup(self):
        """ Tuple or not """
        self.assertRaises(TypeError, Rectangle, (1, ), 1)

    def test_width_rectangle_tup(self):
        """ Tuple or not """
        self.assertRaises(TypeError, Rectangle, (1,), 1)

    def test_height_rectangle_tup(self):
        """ Tuple or not """
        self.assertRaises(TypeError, Rectangle, 1, (1,))

    def test_rectangle(self):
        b1 = Rectangle(1, 3, 4, 6, 84)
        b2 = Rectangle(2, 6, 8, 8, 2)
        self.assertEqual(b1.id, 84)
        self.assertEqual(b1.x, 4)
        self.assertEqual(b1.y, 6)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 3)
        self.assertEqual(b1.area(), 3)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b2.x, 8)
        self.assertEqual(b2.y, 8)
        self.assertEqual(b2.width, 2)
        self.assertEqual(b2.height, 6)
        self.assertEqual(b2.area(), 12)

if __name__ == '__main__':
    unittest.main()
