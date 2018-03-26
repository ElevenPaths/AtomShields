# -*- coding:utf8 -*-
import pytest
import os
from atomshields.checkers import *

class TestCheckers():

    @classmethod
    def setUpClass(cls):
        print("\nRunning unit tests for checkers")


    #################################
    ###        Target-Blank       ###
    #################################

    def test_TargetBlank_root(self):
        checker = TargetBlankChecker()
        checker._path = os.path.join(os.path.dirname(__file__), 'dataset', 'vulnerable')
        issues = checker.run()
        assert len(issues) == 1
        assert issues[0]._file == '/target_blank.html'

    def test_TargetBlank_childdir(self):
        checker = TargetBlankChecker()
        checker._path = os.path.join(os.path.dirname(__file__), 'dataset')
        issues = checker.run()
        assert len(issues) == 1
        assert issues[0]._file == '/vulnerable/target_blank.html'

    def test_TargetBlank_negative(self):
        checker = TargetBlankChecker()
        checker._path = os.path.join(os.path.dirname(__file__), 'dataset', 'notvulnerable')
        issues = checker.run()
        assert len(issues) == 0

    #################################
    ###          DS-Store         ###
    #################################

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

    #################################
    ###          RetireJs         ###
    #################################

    # def test_RetireJS_positive(self):
    #     checker = RetireJSChecker()
    #     checker._path = os.path.join(os.path.dirname(__file__), 'dataset', 'vulnerable')
    #     issues = checker.run()
    #     assert len(issues) == 1
    #     assert issues[0]._file == '/vulnerable_angular.js'

    # def test_RetireJS_negative(self):
    #     checker = RetireJSChecker()
    #     checker._path = os.path.join(os.path.dirname(__file__), 'dataset', 'notvulnerable')
    #     issues = checker.run()
    #     assert len(issues) == 0
