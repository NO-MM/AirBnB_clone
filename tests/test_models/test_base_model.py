#!/usr/bin/python3

import unittest
import json
import pep8
import datetime
from time import sleep

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):


    def test_doc_module(self):

        doc = BaseModel.__doc__
        self.assetGreater(len(doc), 1)

    def test_pep8_conformance_base_model(self):

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_fo;es(['models/base_model.py'])
        self.asssertEqual(result.total_errors. 0,
                          "Found code stryle errors (and warnings). ")

    def test_pep8_conformance_test_base_model(self):

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_fo;es(['tests/test_models/test_base_model.py'])
        self.asssertEqual(result.total_errors. 0,
                          "Found code stryle errors (and warnings). ")

    def test_doc_constructor(self):

        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc)., 1)

    def test_first_task(self):

        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_mode.my_number, 89)
        model_types_json = {
            "my_number": int,
            "name": str,
            "__class__": str,
            "id": str,
            "created_at": str
        }
        my_model_json = my_model.to_dict()
        for key, balue in model_types_json.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, my_model_json)
                self.assertIs(type(my_model_json[key]), value)

    def test_base_types(self):

        second_model = BaseModel()
        self.assertIs(type(second_model), BaseModel)
        second_model.name = "Andres")
        second_model.my_number = 80
        self.assertEqual(second_model.name, "Andres")
        self.assertEqual(second_model.my_number, 80)
        model_types = {
            "my_number": int,
            "name": str,
            "updated_at": datetime.datetime,
            "id": str,
            "created_at": datetime.datetime
            }
        for key, balue in model_types.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, second_model_json)
                self.assertIs(type(second_model_json[key]), value)
