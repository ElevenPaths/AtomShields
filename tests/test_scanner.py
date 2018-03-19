# -*- coding:utf8 -*-
import pytest
import random
import os
from atomshields.scanner import AtomShieldsScanner


class TestScanner():

    @classmethod
    def setUpClass(cls):
        print("\nRunning unit tests for Scanner class")

    # def test_scanner_executeCheckers(self):
    #     atomclass = AtomShieldsScanner('/tmp', True)
    #     print atomclass.executeCheckers()

    def test_scanner_constructor(self):
        atomclass = AtomShieldsScanner('/tmp', True)
        assert atomclass.path == atomclass._path
        assert atomclass.verbose == atomclass.verbose

    ### >>> Is "path" argument neccesary?

    def test_getClassName(self):
        class_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'dataset','class_empty.py')
        atomclass = AtomShieldsScanner('/tmp')
        class_name = atomclass._getClassName(class_path)
        assert 'Chusta' == class_name

    def test_getClassInstance(self):
        class_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'dataset','class_empty.py')
        class_instance = AtomShieldsScanner._getClassInstance(class_path)
        assert class_instance.returnTrue()

    def test_debug(self):
        from test_reports import Capturing
        class_instance = AtomShieldsScanner('/tmp')
        message = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        with Capturing() as output:
            class_instance._debug(message)
        assert message in output

    #################################
    ###           SETTERS         ###
    ### Reminder of domino effect ###
    #################################

    def test_project_attribute(self):
        project = str(random.randrange(1000))
        atomclass = AtomShieldsScanner('/tmp')
        atomclass.project = project
        assert project == atomclass._project

    def test_configFile_attribute(self):
        value = str(random.randrange(1000))
        atomshields = AtomShieldsScanner('/tmp')
        atomshields.configFile = value
        assert os.path.abspath(value) == atomshields.configFile

    def test_config_attribute(self):
        config = {'test': random.randrange(1000)}
        atomclass = AtomShieldsScanner('/tmp')
        atomclass.config = config
        assert config == atomclass._config
