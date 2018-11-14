#!/usr/bin/python3
'''Test Console Module'''
from console import HBNBCommand
from unittest.mock import create_autospec
from uuid import UUID
import models
import unittest
import pep8
import sys
import io
import json
from os import remove
from os.path import isfile
from models.base_model import BaseModel
from datetime import datetime
from io import StringIO


class Test_01_Basic(unittest.TestCase):
    '''Test Console Basic'''

    def setUp(self):
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.out = StringIO()
        sys.stdout = self.out
        self.c = self.create()
        models.storage._FileStorage__objects.clear()

    def teardown(self):
        sys.stdout = sys.__stdout__
        try:
            remove('file.json')
        except:
            pass
        models.storage._FileStorage__objects.clear()
        self.clearIO()

    def clearIO(self):
        self.out.truncate(0)
        self.out.seek(0)

    def create(self, server=None):
        """create console instance"""
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def _last_write(self, nr=None):
        """:return: last `n` output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0],
                           self.mock_stdout.write.call_args_list[-nr:]))

    def test_noinput(self):
        self.assertFalse(self.c.onecmd("\n"))
        self.assertEqual('', self.out.getvalue())

    def test_quit(self):
        """test quit command"""
        self.assertTrue(self.c.onecmd("quit"))
        self.assertTrue(self.c.onecmd("quit some random arguments"))
        self.assertFalse(self.c.onecmd("Quit"))
        self.assertEqual('*** Unknown syntax: Quit\n', self.out.getvalue())
        self.clearIO()

    def test_EOF(self):
        """test EOF"""
        self.assertTrue(self.c.onecmd("EOF"))
        self.assertFalse(self.c.onecmd("eof"))
        self.assertEqual('*** Unknown syntax: eof\n', self.out.getvalue())
        self.clearIO()

    def test_create_fail(self):
        """test create"""
        self.assertFalse(self.c.onecmd('create'))
        self.assertEqual('** class name missing **\n', self.out.getvalue())
        self.clearIO()
        self.assertFalse(self.c.onecmd('create someModel'))
        self.assertEqual("** class doesn't exist **\n", self.out.getvalue())
        self.clearIO()

    def test_creat_success(self):
        """test create success case
        check if output is a valid uuid"""
        self.assertFalse(self.c.onecmd('create BaseModel'))
        testuuid = self.out.getvalue()[:-1]
        uuid_obj = None
        testRes = False
        self.clearIO()
        try:
            uuid_obj = UUID(testuuid)
            testRes = str(uuid_obj) == testuuid
        except:
            testRes = False
        self.assertTrue(testRes)

    def test_all_no_arg(self):
        """test all command with no arg"""
        self.assertFalse(self.c.onecmd('all'))
        self.assertEqual('[]\n', self.out.getvalue())
        self.clearIO()
        self.assertFalse(self.c.onecmd('create BaseModel'))
        self.clearIO()
        self.assertFalse(self.c.onecmd('all'))
        l = json.loads(self.out.getvalue())
        self.clearIO()
        self.assertIsInstance(l, list)
        self.assertEqual(len(l), 1)
        for e in l:
            self.assertIsInstance(e, str)
        self.assertFalse(self.c.onecmd('create BaseModel'))
        self.assertFalse(self.c.onecmd('create User'))
        self.assertFalse(self.c.onecmd('create State'))
        self.clearIO()
        self.assertFalse(self.c.onecmd('all'))
        l = json.loads(self.out.getvalue())
        self.clearIO()
        self.assertIsInstance(l, list)
        self.assertEqual(len(l), 4)
        for e in l:
            self.assertIsInstance(e, str)

    def test_all_with_arg(self):
        """test all command with arg"""
        self.assertFalse(self.c.onecmd('create BaseModel'))
        self.assertFalse(self.c.onecmd('create BaseModel'))
        self.assertFalse(self.c.onecmd('create User'))
        self.clearIO()
        self.assertFalse(self.c.onecmd('all BaseModel'))
        l = json.loads(self.out.getvalue())
        self.clearIO()
        self.assertIsInstance(l, list)
        self.assertEqual(len(l), 2)
        for e in l:
            self.assertIsInstance(e, str)
            self.assertTrue(self.checkObjStrType(e, 'BaseModel'))
        self.assertFalse(self.c.onecmd('all User'))
        l = json.loads(self.out.getvalue())
        self.clearIO()
        self.assertIsInstance(l, list)
        self.assertEqual(len(l), 1)
        for e in l:
            self.assertIsInstance(e, str)
            self.assertTrue(self.checkObjStrType(e, 'User'))
        self.assertFalse(self.c.onecmd('all Amenity'))
        l = json.loads(self.out.getvalue())
        self.clearIO()
        self.assertEqual(l, [])

    def test_update_not_enough_arg(self):
        """test update cmd fail on not enough arguments"""
        self.assertFalse(self.c.onecmd('update'))
        self.assertEqual('** class name missing **\n', self.out.getvalue())
        self.clearIO()
        self.assertFalse(self.c.onecmd('update something'))
        self.assertEqual("** instance id missing **\n", self.out.getvalue())
        self.clearIO()
        self.assertFalse(self.c.onecmd('update something someid'))
        self.assertEqual("** attribute name missing **\n", self.out.getvalue())
        self.clearIO()
        self.assertFalse(self.c.onecmd('update something someid someattr'))
        self.assertEqual("** value missing **\n", self.out.getvalue())

    def test_update_wrong_arg(self):
        """test update fail on wrong arg"""
        self.assertFalse(self.c.onecmd('update something someid atname atval'))
        self.assertEqual("** class doesn't exist **\n", self.out.getvalue())
        self.clearIO()
        self.assertFalse(self.c.onecmd('update BaseModel someid atname atval'))
        self.assertEqual("** no instance found **\n", self.out.getvalue())
        self.clearIO()

    def test_update_newattr(self):
        """test adding attribute to object"""
        self.c.onecmd('create BaseModel')
        objid = self.out.getvalue()[:-1]
        self.clearIO()
        self.assertFalse(
            self.c.onecmd('update BaseModel ' + objid +
                          ' first_name  "Betty"'))
        self.c.onecmd('all BaseModel')
        self.assertTrue("'first_name': 'Betty'" in self.out.getvalue())
        self.clearIO()
        self.assertFalse(
            self.c.onecmd('update BaseModel ' + objid + ' age  "16"'))
        self.c.onecmd('all BaseModel')
        self.assertTrue("'age': 16" in self.out.getvalue())
        self.clearIO()
        self.assertFalse(
            self.c.onecmd('update BaseModel ' + objid + ' number  "5.0"'))
        self.c.onecmd('all BaseModel')
        self.assertTrue("'number': 5.0" in self.out.getvalue())

    def test_update_default_attr(self):
        """test update cmd on existing attribute"""
        self.c.onecmd('create Place')
        objid = self.out.getvalue()[:-1]
        self.clearIO()
        self.assertFalse(
            self.c.onecmd('update Place ' + objid +
                          ' name  "San Francisco"'))
        self.c.onecmd('all Place')
        self.assertTrue("'name': 'San Francisco'" in self.out.getvalue())
        self.clearIO()
        self.assertFalse(
            self.c.onecmd('update Place ' + objid +
                          ' latitude  "90.0"'))
        self.c.onecmd('all Place')
        self.assertTrue("'latitude': 90.0" in self.out.getvalue())
        self.clearIO()
        self.assertFalse(
            self.c.onecmd('update Place ' + objid +
                          ' max_guest  "5"'))
        self.c.onecmd('all Place')
        self.assertTrue("'max_guest': 5" in self.out.getvalue())
        self.clearIO()

    def test_update_too_many_arg(self):
        """test update cmd on too many arguments"""
        self.c.onecmd('create BaseModel')
        objid = self.out.getvalue()[:-1]
        self.clearIO()
        self.assertFalse(
            self.c.onecmd('update BaseModel ' + objid + ' age  "16"' +
                          'number "15.0"'))
        self.c.onecmd('all BaseModel')
        self.assertTrue("'number': 16.0" not in self.out.getvalue())
        self.clearIO()

    def test_show_fail(self):
        """test show fail"""
        self.c.onecmd('create BaseModel')
        bmid = self.out.getvalue()[:-1]
        self.c.onecmd('create BaseModel')
        self.clearIO()
        self.c.onecmd('create User')
        usid = self.out.getvalue()[:-1]
        self.clearIO()
        self.assertFalse(self.c.onecmd('show'))
        self.assertEqual("** class name missing **\n", self.out.getvalue())
        self.clearIO()
        self.assertFalse(self.c.onecmd('show something'))
        self.assertEqual("** instance id missing **\n", self.out.getvalue())
        self.clearIO()
        self.assertFalse(self.c.onecmd('show something someid'))
        self.assertEqual("** class doesn't exist **\n", self.out.getvalue())
        self.clearIO()
        self.assertFalse(self.c.onecmd('show BaseModel 1234'))
        self.assertEqual("** no instance found **\n", self.out.getvalue())
        self.clearIO()
        self.assertFalse(self.c.onecmd('show BaseModel ' + usid))
        self.assertEqual("** no instance found **\n", self.out.getvalue())
        self.clearIO()

    def test_show_success(self):
        """test show success"""
        self.c.onecmd('create BaseModel')
        bmid = self.out.getvalue()[:-1]
        self.c.onecmd('create BaseModel')
        self.clearIO()
        self.c.onecmd('create User')
        usid = self.out.getvalue()[:-1]
        self.clearIO()
        self.assertFalse(self.c.onecmd('show BaseModel ' + bmid))
        self.assertTrue(bmid in self.out.getvalue())
        self.clearIO()
        self.assertFalse(self.c.onecmd('show User ' + usid))
        self.assertTrue(usid in self.out.getvalue())
        self.clearIO()

    @staticmethod
    def checkObjStrType(e, t):
        """check if e is a string representation of type 't'"""
        return (e[e.find('['): e.find(']') + 1] == '[' + t + ']')

if __name__ == '__main__':
    unittest.main()
