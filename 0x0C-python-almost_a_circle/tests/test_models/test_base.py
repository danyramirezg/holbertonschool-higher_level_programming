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

    def test_classBase(self):
