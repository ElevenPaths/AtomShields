# -*- coding:utf8 -*-
import unittest
import os
from atomshields.checkers.passwords import PasswordsCheckers

class TestDSStoreChecker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nRunning unit tests for PASSWORD checker")

    # def test_PASSWORDS_vars(self):
    #     checker = PasswordsCheckers()
    #     checker._path = os.path.join(os.path.dirname(__file__), 'dataset', 'vulnerable')
    #     issues = checker.run()
    #     self.assertEqual(len(issues), 2)
