#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittests for the function def max_integer(list=[])"""

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max__beg(self):
        self.assertEqual(max_integer([5, 2, 3]), 5)

    def test_max_middle(self):
        self.assertEqual(max_integer([1, 8, 3]), 8)

    def test_one_negative(self):
        self.assertEqual(max_integer([1, -8, 3]), 3)

    def test_one_element(self):
        self.assertEqual(max_integer([8]), 8)

    def test_only_negative(self):
        self.assertEqual(max_integer([-1, -8, -3]), -1)

    def test_empty_list(self):
        self.assertEqual(max_integer(), None)
