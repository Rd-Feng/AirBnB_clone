#!/usr/bin/python3
'''Unit Test For FileStorage Engine'''

import unittest
import pep8
import sys
import io
import sys
from models.base_model import BaseModel as BM
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity as Amty
from models.place import Place
from models.review import Review as Rvw
from os import remove
from os.path import isfile
from models.engine.file_storage import FileStorage as FS
from datetime import datetime


class Test_01_FileStorage_Basics(unittest.TestCase):
    '''Tests If FileStorage Meets Basic Specs'''

    def setUp(self):
        '''Setup the FileStorage Module for testing'''
        '''Undo any changes to class attributes'''
        User.email = ''
        User.password = ''
        User.first_name = ''
        User.last_name = ''
        State.name = ''
        City.state_id = ''
        City.name = ''
        Amty.name = ''
        Rvw.place_id = ''
        Rvw.user_id = ''
        Rvw.text = ''
        Place.city_id = ''
        Place.user_id = ''
        Place.name = ''
        Place.description = ''
        Place.number_rooms = 0
        Place.number_bathrooms = 0
        Place.max_guest = 0
        Place.price_by_night = 0
        Place.latitude = 0.0
        Place.longitude = 0.0
        Place.amenity_ids = []
        '''Remove existing file.json'''
        remove("../../file.json")

    def test_01_file_existence(self):
        '''Test if file exists'''
        print("AAAA")
        self.assertTrue(isfile('models/engine/filestorage.py'),
                        'Missing filestorage.py file')

    def test_02_pep8_compliance(self):
        '''Test if file meets pep8 specs'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/filestorage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Fails PEP8 compliance")

    def test_03_method_existence(self):
        '''Test for method existence'''
        clsdir = dir(__import__('models.engine').file_storage.FileStorage)
        self.assertIn('__init__', clsdir, "Missing __init__ method")
        self.assertIn('__str__', clsdir, "Missing __str__ method")
        self.assertIn('save', clsdir, "Missing save method")
        self.assertIn('to_dict', clsdir, "Missing to_dict method")
