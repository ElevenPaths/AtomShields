# -*- coding:utf8 -*-
import pytest
import os
from atomshields.checkers.dsstore import DSStoreChecker

class TestDSStoreChecker():

    @classmethod
    def setUpClass(cls):
        print("\nRunning unit tests for DS_STORE checker")

    def test_DSSTORE_root(self):
        checker = DSStoreChecker()
        checker._path = os.path.join(os.path.dirname(__file__), 'dataset', 'vulnerable')
        issues = checker.run()
        assert len(issues) == 1
        assert issues[0]._file == '/.DS_Store'

    def test_DSSTORE_childdir(self):
        checker = DSStoreChecker()
        checker._path = os.path.join(os.path.dirname(__file__), 'dataset')
        issues = checker.run()
        assert len(issues) == 1
        assert issues[0]._file == '/vulnerable/.DS_Store'

    def test_DSSTORE_negative(self):
        checker = DSStoreChecker()
        checker._path = os.path.join(os.path.dirname(__file__), 'dataset', 'notvulnerable')
        issues = checker.run()
        assert len(issues) == 0
