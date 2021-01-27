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
        """ None value """
        self.assertRaises(TypeError, Rectangle, None, 1)

    def test_height_rectangle_zero(self):
        """ None value """
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
        r1 = Rectangle(1, 3, 4, 6, 84)
        r2 = Rectangle(2, 6, 8, 8, 2)
        self.assertEqual(r1.id, 84)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.area(), 3)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.x, 8)
        self.assertEqual(r2.y, 8)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 6)
        self.assertEqual(r2.area(), 12)

    def test_rectangle_x_coordinate(self):
        """ str error """
        self.assertRaises(TypeError, Rectangle, 2, 3, "x", 5)

    def test_rectangle_y_coordinate(self):
        """ str error """
        self.assertRaises(TypeError, Rectangle, 2, 3, 4, "y")

    def test_rectangle_x_bool(self):
        """ bool error """
        self.assertRaises(TypeError, Rectangle, 2, True, 4, 5)

    def test_rectangle_y_bool(self):
        """ bool error """
        self.assertRaises(TypeError, Rectangle, 2, 3, 4, False)

    def test_rectangle_x_float(self):
        """ float error """
        self.assertRaises(TypeError, Rectangle, 2, 3, 4.5, 5)

    def test_rectangle_y_float(self):
        """ float error """
        self.assertRaises(TypeError, Rectangle, 2, 3, 4, 1.5)

    def test_rectangle_x_tuple(self):
        """ negative error """
        self.assertRaises(ValueError, Rectangle, 2, 3, -4, 5)

    def test_rectangle_y_coordinate(self):
        """ negative error """
        self.assertRaises(ValueError, Rectangle, 2, 3, 4, -5)

    def test_rectangle_x_tuple(self):
        """ tuple error """
        self.assertRaises(TypeError, Rectangle, 2, 3, (4,), 5)

    def test_rectangle_y_coordinate(self):
        """ tuple error """
        self.assertRaises(TypeError, Rectangle, 2, 3, 4, (5,))

    def test_update_rectangle(self):
        r1 = Rectangle(1, 3, 4, 6, 84)
        r2 = Rectangle(5, 6, 10, 10, 5)
        r1.update(19, 18, 17, 16, 15)
        self.assertEqual(r1.id, 19)
        self.assertEqual(r1.x, 16)
        self.assertEqual(r1.y, 15)
        self.assertEqual(r1.width, 18)
        self.assertEqual(r1.height, 17)
        self.assertEqual(r1.area(), 306)
        r1.update(1000, x=1, y=1)
        self.assertEqual(r1.id, 1000)
        self.assertEqual(r1.x, 16)
        self.assertEqual(r1.y, 15)
        r1.update(x=1, y=1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)


if __name__ == '__main__':
    unittest.main()
