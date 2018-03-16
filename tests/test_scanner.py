# -*- coding:utf8 -*-
import unittest
from atomshields.scanner import AtomShieldsScanner
import random
import os

class ScannerTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nRunning unit tests for Scanner class")

    def test_scanner_constructor(self):
        path = '/tmp'
        verbose = True
        atomclass = AtomShieldsScanner(path, verbose)
        self.assertEqual(path, atomclass._path)
        self.assertEqual(verbose, atomclass.verbose)

    ### >>> Is "path" argument neccesary?

    def test_getClassName(self):
        class_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'dataset','class_empty.py')
        atomclass = AtomShieldsScanner('/tmp')
        class_name = atomclass._getClassName(class_path)
        self.assertEqual('Chusta', class_name)

    def test_getClassInstance(self):
        class_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'dataset','class_empty.py')
        class_instance = AtomShieldsScanner._getClassInstance(class_path)
        self.assertTrue(class_instance.returnTrue())


    #################################
    ###           SETTERS         ###
    ### Reminder of domino effect ###
    #################################


    def test_project_attribute(self):
        project = str(random.randrange(1000))
        atomclass = AtomShieldsScanner('/tmp')
        atomclass.project = project
        self.assertEqual(project, atomclass._project)

    def test_configFile_attribute(self):
        value = str(random.randrange(1000))
        atomshields = AtomShieldsScanner('/tmp')
        atomshields.configFile = value
        self.assertEqual(os.path.abspath(value), atomshields.configFile)

    def test_config_attribute(self):
        config = {'test': random.randrange(1000)}
        atomclass = AtomShieldsScanner('/tmp')
        atomclass.config = config
        self.assertEqual(config, atomclass._config)

if __name__ == '__main__':
    unittest.main()
