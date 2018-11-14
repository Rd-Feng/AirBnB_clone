#!/usr/bin/python3
'''Unit Test For FileStorage Engine'''

import unittest
import pep8
import sys
import io
import sys
import json
from os import remove
from os.path import isfile
from models.engine.file_storage import FileStorage as FS
from datetime import datetime
from models.base_model import BaseModel as BM
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity as Amty
from models.place import Place
from models.review import Review as Rvw


def setUpModule():
    '''Set Stuff Up'''
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
    try:
        remove('file.json')
    except:
        pass
    try:
        FS._FileStorage__objects.clear()
    except:
        pass


def tearDownModule():
    '''Tear Stuff Down'''
    try:
        remove('file.json')
    except:
        pass
    try:
        FS._FileStorage__objects.clear()
    except:
        pass


class Test_01_FileStorage_Basics(unittest.TestCase):
    '''Tests If FileStorage Meets Basic Specs'''

    def test_01_file_existence(self):
        '''Test if file exists'''
        self.assertTrue(isfile('models/engine/file_storage.py'),
                        'Missing filestorage.py file')

    def test_02_pep8_compliance(self):
        '''Test if file meets pep8 specs'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Fails PEP8 compliance")

    def test_03_method_existence(self):
        '''Test for method existence'''
        clsdir = dir(__import__('models').engine.file_storage.FileStorage)
        self.assertIn('all', clsdir, "Error missing all method")
        self.assertIn('new', clsdir, "Error missing new method")
        self.assertIn('save', clsdir, "Error missing save method")
        self.assertIn('reload', clsdir, "Error missing reload method")

    def test_04_class_attr_existence_type(self):
        '''Test for class existence and type'''
        try:
            self.assertIsInstance(FS._FileStorage__file_path, str,
                                  "Error __file_path not str")
        except:
            self.fail("Missing private class attribute __file_path")
        try:
            self.assertIsInstance(FS._FileStorage__objects, dict,
                                  "Error __object not dictionary")
        except:
            self.fail("Missing private class attribute __object")

    def test_05_class_attr_defaults(self):
        '''Test class attribute default values'''
        testFS = FS()
        self.assertEqual(testFS._FileStorage__file_path, "file.json",
                         "Error default __file_path not 'file.json'")
        self.assertFalse(testFS._FileStorage__objects,
                         "Error default __object not empty dict")
        del testFS


class Test_02_New_Method(unittest.TestCase):
    '''Test FileStorage New Method'''

    @classmethod
    def setUpClass(cls):
        '''Set Stuff Up for Class'''
        cls.fs_o = FS()

    @classmethod
    def tearDownClass(cls):
        '''Tear Stuff Down for Class'''
        cls.fs_o._FileStorage__objects.clear()
        del cls.fs_o
        try:
            remove('file.json')
        except:
            pass

    def test_01_basic(self):
        '''Test new() method'''
        b_o = BM()
        u_o = User()
        s_o = State()
        c_o = City()
        a_o = Amty()
        p_o = Place()
        r_o = Rvw()
        try:
            type(self).fs_o.new(b_o)
            type(self).fs_o.new(u_o)
            type(self).fs_o.new(s_o)
            type(self).fs_o.new(c_o)
            type(self).fs_o.new(a_o)
            type(self).fs_o.new(p_o)
            type(self).fs_o.new(r_o)
        except:
            self.failed("Failed to add new object to file storage")

    def test_02_count(self):
        '''Test for number of objects in file storage'''
        num = len(type(self).fs_o._FileStorage__objects)
        self.assertEqual(num, 7,
                         "Error incorrect number of objs in file storage")


class Test_03_All_Method(unittest.TestCase):
    '''Test FileStorage All Method'''

    @classmethod
    def setUpClass(cls):
        '''Set Up Stuff for Class'''
        cls.fs_o = FS()
        b_o = BM()
        u_o = User()
        s_o = State()
        c_o = City()
        a_o = Amty()
        p_o = Place()
        r_o = Rvw()
        cls.fs_o.new(b_o)
        cls.fs_o.new(u_o)
        cls.fs_o.new(s_o)
        cls.fs_o.new(c_o)
        cls.fs_o.new(a_o)
        cls.fs_o.new(p_o)
        cls.fs_o.new(r_o)

    @classmethod
    def tearDownClass(cls):
        '''Tear Stuff Down for Class'''
        cls.fs_o._FileStorage__objects.clear()
        del cls.fs_o
        try:
            remove('file.json')
        except:
            pass

    def test_01_is_dict(self):
        '''Test all outputs dictionary'''
        dct = type(self).fs_o.all()
        self.assertIsInstance(dct, dict,
                              "Error All() does not output a dictionary")

    def test_02_num_in_dict(self):
        '''Test number of items in dictionary'''
        num = len(type(self).fs_o.all())
        self.assertEqual(num, 7,
                         "Error incorrect number of items in All output")


class Test_04_Save_Method(unittest.TestCase):
    '''Test FileStorage Save Method'''

    @classmethod
    def setUpClass(cls):
        '''Set Stuff Up for Class'''
        cls.fs_o = FS()
        b_o = BM()
        u_o = User()
        s_o = State()
        c_o = City()
        a_o = Amty()
        p_o = Place()
        r_o = Rvw()
        cls.fs_o.new(b_o)
        cls.fs_o.new(u_o)
        cls.fs_o.new(s_o)
        cls.fs_o.new(c_o)
        cls.fs_o.new(a_o)
        cls.fs_o.new(p_o)
        cls.fs_o.new(r_o)

    @classmethod
    def tearDownClass(cls):
        '''Tear Stuff Down for Class'''
        cls.fs_o._FileStorage__objects.clear()
        del cls.fs_o
        try:
            remove('file.json')
        except:
            pass

    def test_01_basic(self):
        '''Test if save works'''
        try:
            type(self).fs_o.save()
        except:
            self.fail("Failed to save file")

    def test_02_file_existence(self):
        '''Test if save file exists'''
        self.assertTrue(isfile('file.json'), "Error missing file.json file")

    def test_03_file_read(self):
        '''Test file contents'''
        filename = type(self).fs_o._FileStorage__file_path
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.loads(f.readline())
        except:
            self.fail("Failed to read from file")
        self.assertIsInstance(data, dict,
                              "Error data not saved for json conversion")
        self.assertEqual(len(data), 7,
                         "Error incorrect number of items written to file")
        for k, v in data.items():
            cls1, uid1 = k.split('.')[0], k.split('.')[1]
            try:
                cls2 = v['__class__']
                uid2 = v['id']
            except:
                self.fail("Error file incorrectly written")
            self.assertEqual(cls1, cls2,
                             "Error file incorrectly written")
            self.assertEqual(uid1, uid2,
                             "Error file incorrectly written")
            try:
                raw_dt1 = v['created_at']
                raw_dt2 = v['updated_at']
            except:
                self.fail("Error file incorrectly written")
            try:
                dt1 = datetime.strptime(raw_dt1, "%Y-%m-%dT%H:%M:%S.%f")
                dt2 = datetime.strptime(raw_dt2, "%Y-%m-%dT%H:%M:%S.%f")
            except:
                self.fail("Error file incorrectly written")
            self.assertIsInstance(dt1, datetime,
                                  "Error file incorrectly written")
            self.assertIsInstance(dt2, datetime,
                                  "Error file incorrectly written")


class Test_05_Reload_Method(unittest.TestCase):
    '''Test FileStorage Reload Method'''

    @classmethod
    def setUpClass(cls):
        '''Set Stuff Up for Class'''
        cls.fs_o = FS()
        b_o = BM()
        u_o = User()
        s_o = State()
        c_o = City()
        a_o = Amty()
        p_o = Place()
        r_o = Rvw()
        cls.fs_o.new(b_o)
        cls.fs_o.new(u_o)
        cls.fs_o.new(s_o)
        cls.fs_o.new(c_o)
        cls.fs_o.new(a_o)
        cls.fs_o.new(p_o)
        cls.fs_o.new(r_o)
        cls.fs_o.save()

    @classmethod
    def tearDownClass(cls):
        '''Tear Stuff Down for Class'''
        cls.fs_o._FileStorage__objects.clear()
        del cls.fs_o
        try:
            remove('file.json')
        except:
            pass

    def test_01_basic(self):
        '''Test reload'''
        pass
