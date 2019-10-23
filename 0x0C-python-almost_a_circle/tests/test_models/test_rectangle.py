#!/usr/bin/python3
"""
Unittest cases for Rectangle class
"""

import unittest
import io
from models.base import Base
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """Class rectangle test"""

    def test_id(self):
        """Test to check the id"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(2, 4)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 2)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_widthProperty(self):
        # Test the property of width

        r1 = Rectangle(2, 4)
        self.assertEqual(r1.width, 2)

    def test_heightProperty(self):
        # Test the property of height

        r1 = Rectangle(2, 4)
        self.assertEqual(r1.height, 4)

    def test_xProperty(self):
        # Test the property of x

        r = Rectangle(2, 4, 3, 2)
        self.assertEqual(r.x, 3)

    def test_yProperty(self):
        # Test the property of y

        r = Rectangle(2, 4, 3, 2)
        self.assertEqual(r.y, 2)

    def test_heightSetter(self):
        # Test if height is not a integer

        self.assertRaises(TypeError, Rectangle, 4, "Dany")

    def test_heightNegative(self):
        # Test if the height is a negative number

        self.assertRaises(ValueError, Rectangle, 4, -8)

    def test_widthSetter(self):
        # Test if width is not a integer

        self.assertRaises(TypeError, Rectangle, "Dany", 10)

    def test_widthNegative(self):
        # Test if the weight is a negative number

        self.assertRaises(ValueError, Rectangle, -4, 8)

    def test_xSetter(self):
        # Test if x is not a integer

        self.assertRaises(TypeError, Rectangle, 8, 10, "Dany", 2)

    def test_xNegative(self):
        # Test if the x is a negative number

        self.assertRaises(ValueError, Rectangle, 10, 8, -4, 2)

    def test_ySetter(self):
        # Test if y is not a integer

        self.assertRaises(TypeError, Rectangle, 8, 10, 2, "Dany")

    def test_yNegative(self):
        # Test if the y is a negative number

        self.assertRaises(ValueError, Rectangle, 10, 8, 4, -2)

    def testArea(self):
        # Test the method area:

        r1 = Rectangle(2, 3)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(4, 6, 2, 0)
        self.assertEqual(r2.area(), 24)
        r3 = Rectangle(8888888888, 999999999)
        self.assertEqual(r3.area(), 8888888888 * 999999999)

    def test_areaError(self):
        # Test the area when there are not arguments

        self.assertRaises(TypeError, Rectangle)

    def test_documentation(self):
        # Test to verify if the documentation is created

        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(hasattr(Rectangle, "height"))
        self.assertTrue(Rectangle.height.__doc__)
        self.assertTrue(hasattr(Rectangle, "width"))
        self.assertTrue(Rectangle.width.__doc__)
        self.assertTrue(hasattr(Rectangle, "x"))
        self.assertTrue(Rectangle.x.__doc__)
        self.assertTrue(hasattr(Rectangle, "y"))
        self.assertTrue(Rectangle.y.__doc__)
        self.assertTrue(hasattr(Rectangle, "area"))
        self.assertTrue(Rectangle.area.__doc__)
        self.assertTrue(hasattr(Rectangle, "display"))
        self.assertTrue(Rectangle.display.__doc__)
        self.assertTrue(hasattr(Rectangle, "__str__"))
        self.assertTrue(Rectangle.__str__.__doc__)
        self.assertTrue(hasattr(Rectangle, "update"))
        self.assertTrue(Rectangle.update.__doc__)
        self.assertTrue(hasattr(Rectangle, "to_dictionary"))
        self.assertTrue(Rectangle.to_dictionary.__doc__)

#     def test_width_private(self):
#         with self.assertRaises(AttributeError):
#             print(Rectangle(5, 5, 0, 0, 1).__width)
#
#     def test_height_private(self):
#         with self.assertRaises(AttributeError):
#             print(Rectangle(5, 5, 0, 0, 1).__height)
#
#     def test_x_private(self):
#         with self.assertRaises(AttributeError):
#             print(Rectangle(5, 5, 0, 0, 1).__x)
#
#     def test_y_private(self):
#         with self.assertRaises(AttributeError):
#             print(Rectangle(5, 5, 0, 0, 1).__y)
#
#     def test_width_getter(self):
#         r = Rectangle(5, 7, 7, 5, 1)
#         self.assertEqual(5, r.width)
#
#     def test_width_setter(self):
#         r = Rectangle(5, 7, 7, 5, 1)
#         r.width = 10
#         self.assertEqual(10, r.width)
#
#     def test_height_getter(self):
#         r = Rectangle(5, 7, 7, 5, 1)
#         self.assertEqual(7, r.height)
#
#     def test_height_setter(self):
#         r = Rectangle(5, 7, 7, 5, 1)
#         r.height = 10
#         self.assertEqual(10, r.height)
#
#     def test_x_getter(self):
#         r = Rectangle(5, 7, 7, 5, 1)
#         self.assertEqual(7, r.x)
#
#     def test_x_setter(self):
#         r = Rectangle(5, 7, 7, 5, 1)
#         r.x = 10
#         self.assertEqual(10, r.x)
#
#     def test_y_getter(self):
#         r = Rectangle(5, 7, 7, 5, 1)
#         self.assertEqual(5, r.y)
#
#     def test_y_setter(self):
#         r = Rectangle(5, 7, 7, 5, 1)
#         r.y = 10
#         self.assertEqual(10, r.y)
#
#
# class TestRectangle_width(unittest.TestCase):
#     """Unittests for testing initialization of Rectangle width attribute."""
#
#     def test_None_width(self):
#         with self.assertRaisesRegex(TypeError, "width must be an integer"):
#             Rectangle(None, 2)
#
#     def test_str_width(self):
#         with self.assertRaisesRegex(TypeError, "width must be an integer"):
#             Rectangle("invalid", 2)
#
#     def test_float_width(self):
#         with self.assertRaisesRegex(TypeError, "width must be an integer"):
#             Rectangle(5.5, 1)
#
#     def test_complex_width(self):
#         with self.assertRaisesRegex(TypeError, "width must be an integer"):
#             Rectangle(complex(5), 2)
#
#     def test_dict_width(self):
#         with self.assertRaisesRegex(TypeError, "width must be an integer"):
#             Rectangle({"a": 1, "b": 2}, 2)
#
#     def test_bool_width(self):
#         with self.assertRaisesRegex(TypeError, "width must be an integer"):
#             Rectangle(True, 2)
#
#     def test_list_width(self):
#         with self.assertRaisesRegex(TypeError, "width must be an integer"):
#             Rectangle([1, 2, 3], 2)
#
#     def test_set_width(self):
#         with self.assertRaisesRegex(TypeError, "width must be an integer"):
#             Rectangle({1, 2, 3}, 2)
#
#     def test_tuple_width(self):
#         with self.assertRaisesRegex(TypeError, "width must be an integer"):
#             Rectangle((1, 2, 3), 2)
#
#     def test_frozenset_width(self):
#         with self.assertRaisesRegex(TypeError, "width must be an integer"):
#             Rectangle(frozenset({1, 2, 3, 1}), 2)
#
#  if __name__ == "__main__":
#   unittest.main()
