#!/usr/bin/python3
'''Test Console Module'''
from console import HBNBCommand
from unittest.mock import create_autospec
import unittest
import pep8
import sys
import io
import sys
import models
import json
from os import remove
from os.path import isfile
from models.base_model import BaseModel
from datetime import datetime


class Test_01_Basic(unittest.TestCase):
    '''Test Console Basic'''
    def setUp(self):
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

if __name__ == '__main__':
    unittest.main()
