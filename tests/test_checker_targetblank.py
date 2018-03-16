# -*- coding:utf8 -*-
import unittest
import os
from atomshields.checkers.targetblank import TargetBlankChecker

class TestTargetBlankChecker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nRunning unit tests for TargetBlank checker")

    def test_TargetBlank_root(self):
        checker = TargetBlankChecker()
        checker._path = os.path.join(os.path.dirname(__file__), 'dataset', 'vulnerable')
        issues = checker.run()
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]._file, '/target_blank.html')

    def test_TargetBlank_childdir(self):
        checker = TargetBlankChecker()
        checker._path = os.path.join(os.path.dirname(__file__), 'dataset')
        issues = checker.run()
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]._file, '/vulnerable/target_blank.html')

    def test_TargetBlank_negative(self):
        checker = TargetBlankChecker()
        checker._path = os.path.join(os.path.dirname(__file__), 'dataset', 'notvulnerable')
        issues = checker.run()
        self.assertFalse(len(issues))

if __name__ == '__main__':
    unittest.main()
