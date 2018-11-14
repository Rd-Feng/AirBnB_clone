#!/usr/bin/python3
'''Unit Test For State Model'''

import unittest
import pep8
import sys
import io
import sys
import models
from os import remove
from os.path import isfile
from models.state import State
from datetime import datetime


def setUpModule():
    '''Set Stuff Up'''
    models.storage._FileStorage__objects.clear()
    try:
        remove(models.storage._FileStorage__file_path)
    except:
        pass


def tearDownModule():
    '''Tear Stuff Down'''
    models.storage._FileStorage__objects.clear()
    try:
        remove(models.storage._FileStorage__file_path)
    except:
        pass


class Test_01_State_Basics(unittest.TestCase):
    '''Tests If State Meets Basic Specs'''

    def test_01_file_existence(self):
        '''Test if file exists'''
        self.assertTrue(isfile('models/state.py'),
                        'Missing state.py file')

    def test_02_pep8_compliance(self):
        '''Test if file meets pep8 specs'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Fails PEP8 compliance")

    def test_03_method_existence(self):
        '''Test for method existence'''
        clsdir = dir(__import__('models').state.State)
        self.assertIn('__init__', clsdir, "Missing __init__ method")
        self.assertIn('__str__', clsdir, "Missing __str__ method")
        self.assertIn('save', clsdir, "Missing save method")
        self.assertIn('to_dict', clsdir, "Missing to_dict method")

    def test_04_instantiation(self):
        '''Test for failed instantiation'''
        try:
            obj1 = State()
            obj2 = State('Test')
            obj3 = State('id')
            obj4 = State(888)
            obj5 = State(id="1234")
            obj6 = State([1, 'A', 3])
            obj7 = State({'A': 1, 'B': 2})
            obj8 = State((2, 'B', 6))
            obj9 = State({7, 'HI', 10})
            obj10 = State(None)
            obj11 = State(-666)
            obj12 = State(float('nan'))
            obj13 = State(float('inf'))
            obj14 = State('')
            obj15 = State([])
            obj16 = State([-5])
            obj17 = State({})
            obj18 = State({'u': [6, 7]})
        except:
            self.fail("Failed State instantiation")
        finally:
            del obj1
            del obj2
            del obj3
            del obj4
            del obj5
            del obj6
            del obj7
            del obj8
            del obj9
            del obj10
            del obj11
            del obj12
            del obj13
            del obj14
            del obj15
            del obj16
            del obj17
            del obj18

    def test_05_instance_class_match(self):
        '''Test if instanced object matches class'''
        obj1 = State()
        self.assertIsInstance(obj1, State,
                              "Instanced object is not State class")
        del obj1

    def test_06_attr_existence(self):
        '''Test for public attribute existence'''
        obj1 = State()
        self.assertIsInstance(obj1.id, str,
                              "Instanced object.id not a string type")
        self.assertIsInstance(obj1.created_at, datetime,
                              "Instanced object.created_at not datetime type")
        self.assertIsInstance(obj1.updated_at, datetime,
                              "Instanced object.updated_at not datetime type")
        del obj1

    def test_07_cls_attr_type(self):
        '''Test State Class Attribute Types'''
        obj = State()
        self.assertIsInstance(type(obj).name, str,
                              "Error name not str type")
        del obj

    def test_07_dynamic_attr(self):
        '''Test to dynamically add attributes'''
        obj1 = State()
        try:
            obj1.test1 = 'TEST'
            obj1.test2 = [1, 2, 3]
            obj1.test3 = {'a': 1, 'b': 2, 'c': 3}
            obj1.test4 = (4, 5, 6)
            obj1.test5 = {7, 8, 9}
            obj1.test6 = None
            obj1.test7 = 0.0
            obj1.test8 = float('nan')
            obj1.test9 = float('inf')
            obj1.test10 = -666
            obj1.test11 = ''
            obj1.test12 = []
            obj1.test13 = [-5]
            obj1.test14 = {}
            obj1.test15 = {'u': [6, 7]}
        except:
            self.fail("Failed to dynamically add pub inst attributes")
        self.assertEqual(obj1.__dict__['test1'], 'TEST',
                         "Failed to assign value to dynamic pub inst attr")
        self.assertEqual(obj1.__dict__['test2'], [1, 2, 3],
                         "Failed to assign value to dynamic pub inst attr")
        self.assertEqual(obj1.__dict__['test3'], {'a': 1, 'b': 2, 'c': 3},
                         "Failed to assign value to dynamic pub inst attr")
        self.assertEqual(obj1.__dict__['test4'], (4, 5, 6),
                         "Failed to assign value to dynamic pub inst attr")
        self.assertEqual(obj1.__dict__['test5'], {7, 8, 9},
                         "Failed to assign value to dynamic pub inst attr")
        self.assertEqual(obj1.__dict__['test6'], None,
                         "Failed to assign value to dynamic pub inst attr")
        self.assertEqual(obj1.__dict__['test7'], 0.0,
                         "Failed to assign value to dynamic pub inst attr")
        self.assertNotEqual(obj1.__dict__['test8'], float('nan'),
                            "Failed to assign value to dynamic pub inst attr")
        self.assertEqual(obj1.__dict__['test9'], float('inf'),
                         "Failed to assign value to dynamic pub inst attr")
        self.assertEqual(obj1.__dict__['test10'], -666,
                         "Failed to assign value to dynamic pub inst attr")
        self.assertEqual(obj1.__dict__['test11'], '',
                         "Failed to assign value to dynamic pub inst attr")
        self.assertEqual(obj1.__dict__['test12'], [],
                         "Failed to assign value to dynamic pub inst attr")
        self.assertEqual(obj1.__dict__['test13'], [-5],
                         "Failed to assign value to dynamic pub inst attr")
        self.assertEqual(obj1.__dict__['test14'], {},
                         "Failed to assign value to dynamic pub inst attr")
        self.assertEqual(obj1.__dict__['test15'], {'u': [6, 7]},
                         "Failed to assign value to dynamic pub inst attr")
        self.assertEqual(len(obj1.__dict__), 18)
        del obj1

    def test_08_class_attr_defaults(self):
        '''Test class attributes'''
        self.assertEqual(State.name, '',
                         "Error State class name default not empty")

    def test_09_class_attr_assignment(self):
        '''Test class attr assignment'''
        State.name = 'California'
        obj1 = State()
        self.assertEqual(type(obj1).name, 'California',
                         "Error incorrect name assignment")
        del obj1


class Test_02_State_Constuctor(unittest.TestCase):
    '''Test State Constructor'''

    @classmethod
    def setUpClass(cls):
        '''Setup Class'''
        cls.obj1 = State()
        cls.obj2 = State()
        cls.obj3 = State()

    @classmethod
    def tearDownClass(cls):
        '''Tear Down Class'''
        del cls.obj1
        del cls.obj2
        del cls.obj3

    def test_01_key_existence(self):
        '''Test for basic key existence'''
        self.assertIn('id', dir(type(self).obj1), "Missing id key")
        self.assertIn('created_at', dir(type(self).obj1),
                      "Missing created_at key")
        self.assertIn('updated_at', dir(type(self).obj1),
                      "Missing updated_at key")

    def test_02_id_generation(self):
        '''Test for different generated IDs'''
        self.assertNotEqual(type(self).obj1.id, type(self).obj2.id,
                            "Fail: Same ID")
        self.assertNotEqual(type(self).obj2.id, type(self).obj3.id,
                            "Fail: Same ID")
        self.assertNotEqual(type(self).obj1.id, type(self).obj3.id,
                            "Fail: Same ID")

    def test_03_datetime(self):
        '''Test for same datetime'''
        self.assertEqual(type(self).obj1.created_at,
                         type(self).obj1.updated_at,
                         "Fail: Different date times")
        self.assertEqual(type(self).obj2.created_at,
                         type(self).obj2.updated_at,
                         "Fail: Different date times")
        self.assertEqual(type(self).obj3.created_at,
                         type(self).obj3.updated_at,
                         "Fail: Different date times")


class Test_04_State_Str(unittest.TestCase):
    '''Test State __str___'''

    @classmethod
    def setUpClass(cls):
        '''Set Up Class'''
        cls.obj1 = State(id="1234-5678-9012",
                         created_at="1234-05-06T01:23:45.678901",
                         updated_at="9999-11-11T11:11:22.222222")
        cls.god1 = '[State]'
        cls.god2 = '(1234-5678-9012)'

    @classmethod
    def tearDownClass(cls):
        '''Tear Down Class'''
        del cls.obj1

    def test_01_str_return_type(self):
        '''Test __str__ return value'''
        out = type(self).obj1.__str__()
        self.assertIsInstance(out, str,
                              "Error __str__ incorrect return type")

    def test_02_str_format(self):
        '''Test __str__ format'''
        out1 = type(self).obj1.__str__().split(' ', 2)[0]
        out2 = type(self).obj1.__str__().split(' ', 2)[1]
        self.assertEqual(out1, type(self).god1,
                         "Class name does not match in __str__ output")
        self.assertEqual(out2, type(self).god2,
                         "ID does not match in __str__ output")

    def test_03_str_return_dynamic_attr_ret_type(self):
        '''Test __str__ return with dynamic attr'''
        type(self).obj1.test1 = 'TEST'
        type(self).obj1.test2 = [1, 2, 3]
        out = type(self).obj1.__str__()
        self.assertIsInstance(out, str,
                              "Error improper __str__ return type")


class Test_05_State_Save(unittest.TestCase):
    '''Test State Save Method'''

    def test_01_save_datetime(self):
        '''Check for update datetime change after save'''
        models.storage.all().clear()
        obj1 = State()
        old_ua = obj1.updated_at
        try:
            obj1.save()
        except:
            self.fail("Failed to save")
        new_ua = obj1.updated_at
        self.assertNotEqual(old_ua, new_ua,
                            "Failed to change updated at datetime")
        del obj1

    def test_02_save_consistency(self):
        '''Check for consistency after save'''
        models.storage.all().clear()
        obj1 = State()
        old = obj1.__dict__.copy()
        try:
            obj1.save()
        except:
            self.fail("Failed to save")
        new = obj1.__dict__.copy()
        del old['updated_at']
        del new['updated_at']
        self.assertEqual(old, new,
                         "Failed to maintain consistency after save")
        del obj1


class Test_06_State_To_Dict(unittest.TestCase):
    '''Test State To_Dict Method'''

    def setUp(self):
        '''Set Up'''
        self.dct1 = State().to_dict()
        self.dct2 = State().to_dict()

    def test_01_is_dict_type(self):
        '''Test to_dict simple'''
        self.assertIsInstance(self.dct1, dict,
                              "Failed to_dict does not prodice dictionary"
                              " type")

    def test_02_required_keys(self):
        '''Test for proper output format'''
        key_list = self.dct1.keys()
        self.assertIn('id', key_list, "Error 'id' not in to_dict() output")
        self.assertIn('created_at', key_list,
                      "Error 'created_by' not in to_dict() output")
        self.assertIn('updated_at', key_list,
                      "Error 'updated_at' not in to_dict() output")
        self.assertIn('__class__', key_list,
                      "Error '__class__' not in to_dict() output")

    def test_03_value_type(self):
        '''Test for proper value format'''
        value_list = self.dct1.values()
        for e in value_list:
            self.assertIsInstance(e, str, "Error to_dict has non-str value")

    def test_04_classname_value(self):
        '''Test if class name is properly stored'''
        self.assertEqual('State', self.dct1['__class__'],
                         "Error incorrect key for BaseModel")

    def test_05_different_to_dict(self):
        '''Test for different outputs'''
        self.assertNotEqual(self.dct1, self.dct2,
                            "Error to_dict does not produce different output")


if __name__ == '__main__':
    unittest.main()
