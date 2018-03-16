# -*- coding:utf8 -*-
import pytest
import os
from atomshields.checkers.targetblank import TargetBlankChecker

class TestTargetBlankChecker():

    @classmethod
    def setUpClass(cls):
        print("\nRunning unit tests for TargetBlank checker")

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
