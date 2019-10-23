#!/usr/bin/python3
"""Unittest cases for Base class"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    """class base test"""

    def test_id(self):
        """
        Test to check the id
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(8)
        self.assertEqual(b2.id, 8)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_isInstance(self):
        """
        Test if 'ins' is an object
        """
        ins = Base()
        self.assertIsInstance(ins, object)

    def test_documentation(self):
        """
        Test to see if documentation is
        created and correct
        """
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(Square.__init__.__doc__)
        self.assertTrue(hasattr(Square, "size"))
        self.assertTrue(Square.size.__doc__)
        self.assertTrue(hasattr(Square, "x"))
        self.assertTrue(Square.x.__doc__)
        self.assertTrue(hasattr(Square, "y"))
        self.assertTrue(Square.y.__doc__)
        self.assertTrue(hasattr(Square, "__str__"))
        self.assertTrue(Square.__str__.__doc__)
        self.assertTrue(hasattr(Square, "update"))
        self.assertTrue(Square.update.__doc__)
        self.assertTrue(hasattr(Square, "to_dictionary"))
        self.assertTrue(Square.to_dictionary.__doc__)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("Dany", Base("Dany").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)
