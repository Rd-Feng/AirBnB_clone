#!/usr/bin/python3
import unittest
import pep8
from os.path import isfile
from models.base_model import BaseModel

'''Unit Test For Base Model'''


class Test_BaseModel_Basics(unittest.TestCase):
    '''Tests If BaseModel Meets Basic Specs'''

    def test_file_existence(self):
        '''Test if file exists'''
        self.assertTrue(isfile('models/base_model.py'),
                        'Missing base_model.py file')

    def test_pep8_compliance(self):
        '''Test if file meets pep8 specs'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Fails PEP8 compliance")

    def test_method_existence(self):
        '''Test for method existence'''
        clsdir = dir(__import__('models').base_model.BaseModel)
        self.assertIn('__init__', clsdir, "Missing __init__ method")
        self.assertIn('__str__', clsdir, "Missing __str__ method")
        self.assertIn('save', clsdir, "Missing save method")
        self.assertIn('to_dict', clsdir, "Missing to_dict method")

    def test_docstring_existence(self):
        '''Test for docstring existence'''
        mod = __import__('models').base_model
        self.assertIsNotNone(mod.__doc__, "Missing module docstring")
        cname = mod.BaseModel
        self.assertIsNotNone(cname.__doc__, "Missing class docstring")
        self.assertIsNotNone(cname.__init__.__doc__,
                             "Missing __init__ docstring")
        self.assertIsNotNone(cname.__str__.__doc__,
                             "Missing __str__ docstring")
        self.assertIsNotNone(cname.save.__doc__, "Missing save docstring")
        self.assertIsNotNone(cname.to_dict.__doc__, "Missing to_dict docstring")

class Test_BaseModel_Constuctor(unittest.TestCase):
    '''Test BaseModel Constructor'''

    def test_something(self):
        '''Testing Something'''
        test_obj1 = BaseModel()
        test_obj2 = BaseModel()
        self.assertNotEqual(test_obj1.id, test_obj2.id, "WUT?!")

if __name__ == '__main__':
    unittest.main()
