#!/usr/bin/python3
import unittest
import json
import pep8
from models.base import Base
from models.rectangle import Rectangle

"""
Unittest cases for Base class
"""


class BaseTest(unittest.TestCase):

    def test1_id(self):
        """
        Test to check the id
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(8)
        self.assertEqual(b2.id, 8)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test2_isInstance(self
                         ):
        """
        Test if 'ins' is an object
        """
        ins = Base()
        self.assertIsInstance(ins, object)

    #def test3_



