#!/usr/bin/python3
'''Unit Test For User Model'''

import unittest
import pep8
import sys
import io
import sys
import models
from os import remove
from os.path import isfile
from models.user import User
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


class Test_01_User_Basics(unittest.TestCase):
    '''Tests If User Meets Basic Specs'''

    def test_01_file_existence(self):
        '''Test if file exists'''
        self.assertTrue(isfile('models/user.py'),
                        'Missing user.py file')

    def test_02_pep8_compliance(self):
        '''Test if file meets pep8 specs'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Fails PEP8 compliance")

    def test_03_method_existence(self):
        '''Test for method existence'''
        clsdir = dir(__import__('models').user.User)
        self.assertIn('__init__', clsdir, "Missing __init__ method")
        self.assertIn('__str__', clsdir, "Missing __str__ method")
        self.assertIn('save', clsdir, "Missing save method")
        self.assertIn('to_dict', clsdir, "Missing to_dict method")

    def test_04_instantiation(self):
        '''Test for failed instantiation'''
        try:
            obj1 = User()
            obj2 = User('Test')
            obj3 = User('id')
            obj4 = User(888)
            obj5 = User(id="1234")
            obj6 = User([1, 'A', 3])
            obj7 = User({'A': 1, 'B': 2})
            obj8 = User((2, 'B', 6))
            obj9 = User({7, 'HI', 10})
            obj10 = User(None)
            obj11 = User(-666)
            obj12 = User(float('nan'))
            obj13 = User(float('inf'))
            obj14 = User('')
            obj15 = User([])
            obj16 = User([-5])
            obj17 = User({})
            obj18 = User({'u': [6, 7]})
        except:
            self.fail("Failed User instantiation")
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
        obj1 = User()
        self.assertIsInstance(obj1, User,
                              "Instanced object is not User class")
        del obj1

    def test_06_attr_existence(self):
        '''Test for public attribute existence'''
        obj1 = User()
        self.assertIsInstance(obj1.id, str,
                              "Instanced object.id not a string type")
        self.assertIsInstance(obj1.created_at, datetime,
                              "Instanced object.created_at not datetime type")
        self.assertIsInstance(obj1.updated_at, datetime,
                              "Instanced object.updated_at not datetime type")
        del obj1

    def test_07_cls_attr_type(self):
        '''Test User Class Attribute Types'''
        obj = User()
        self.assertIsInstance(type(obj).email, str,
                              "Error email not str type")
        self.assertIsInstance(type(obj).password, str,
                              "Error password not str type")
        self.assertIsInstance(type(obj).first_name, str,
                              "Error first_name not str type")
        self.assertIsInstance(type(obj).last_name, str,
                              "Error last_name not str type")
        del obj

    def test_07_dynamic_attr(self):
        '''Test to dynamically add attributes'''
        obj1 = User()
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
        self.assertEqual(User.email, '',
                         "Error User class email default not empty")
        self.assertEqual(User.password, '',
                         "Error User class password default not empty")
        self.assertEqual(User.first_name, '',
                         "Error User class first_name default not empty")
        self.assertEqual(User.last_name, '',
                         "Error User class last_name default not empty")

    def test_09_class_attr_assignment(self):
        '''Test class attr assignment'''
        User.email = 'test@test.test'
        obj1 = User()
        self.assertEqual(type(obj1).email, 'test@test.test',
                         "Error incorrect email assignment")
        User.password = 'password123'
        self.assertEqual(type(obj1).password, 'password123',
                         "Error incorrect password assignment")
        User.first_name = 'FIRSTname'
        self.assertEqual(type(obj1).first_name, 'FIRSTname',
                         "Error incorrect first_name assignment")
        User.last_name = 'lastNAME'
        self.assertEqual(type(obj1).last_name, 'lastNAME',
                         "Error incorrect last_name assignment")
        del obj1


class Test_02_User_Constuctor(unittest.TestCase):
    '''Test User Constructor'''

    @classmethod
    def setUpClass(cls):
        '''Setup Class'''
        cls.obj1 = User()
        cls.obj2 = User()
        cls.obj3 = User()

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


class Test_04_User_Str(unittest.TestCase):
    '''Test User __str___'''

    @classmethod
    def setUpClass(cls):
        '''Set Up Class'''
        cls.obj1 = User(id="1234-5678-9012",
                        created_at="1234-05-06T01:23:45.678901",
                        updated_at="9999-11-11T11:11:22.222222")
        cls.god1 = '[User]'
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


class Test_05_User_Save(unittest.TestCase):
    '''Test User Save Method'''

    def test_01_save_datetime(self):
        '''Check for update datetime change after save'''
        models.storage.all().clear()
        obj1 = User()
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
        obj1 = User()
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


class Test_06_User_To_Dict(unittest.TestCase):
    '''Test User To_Dict Method'''

    def setUp(self):
        '''Set Up'''
        self.dct1 = User().to_dict()
        self.dct2 = User().to_dict()

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
        self.assertEqual('User', self.dct1['__class__'],
                         "Error incorrect key for BaseModel")

    def test_05_different_to_dict(self):
        '''Test for different outputs'''
        self.assertNotEqual(self.dct1, self.dct2,
                            "Error to_dict does not produce different output")


if __name__ == '__main__':
    unittest.main()
