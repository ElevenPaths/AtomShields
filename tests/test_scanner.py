# -*- coding:utf8 -*-
import pytest
import random
import os
from test_reports import Capturing
from atomshields import AtomShieldsScanner, Issue

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
        atomclass = AtomShieldsScanner('/tmp')
        message = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        with Capturing() as output:
            atomclass._debug(message)
        assert message in output



    #################################
    ###           CONFIG          ###
    #################################

    def test_getConfig_file(self):
        atomclass = AtomShieldsScanner('/tmp')
        conf_file = os.path.join(os.path.abspath(os.path.dirname(__file__)),'dataset','configFile')
        atomclass._config_file = conf_file
        atomclass.loadConfig()
        conf = atomclass.getConfig()
        assert conf['Checker1']['enabled'] == 'True'

    def test_getConfig_section(self):
        atomclass = AtomShieldsScanner('/tmp')
        conf_file = os.path.join(os.path.abspath(os.path.dirname(__file__)),'dataset','configFile')
        atomclass._config_file = conf_file
        atomclass.loadConfig()
        conf = atomclass.getConfig('Checker2')
        assert conf['name'] == 'Checker Two'

    # def test_generateConfig(self):
    #     atomclass = AtomShieldsScanner('/tmp')
    #     cur_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'CONFIGFILE.conf')
    #     atomclass.generateConfig(True)

    def test_checkProperties_path(self):
        atomclass = AtomShieldsScanner('/tmp')
        atomclass.project = 'Chusta'
        atomclass.checkProperties()
        return True

    def test_checkProperties_project(self):
        atomclass = AtomShieldsScanner('/tmp')
        try:
            atomclass.checkProperties()
            raise AssertionError('atomclass.project should not be setted')
        except Exception as e:
            assert e.message == 'Project is required'

    def test_showSummary(self):
        str_format = "%-20s\t0"
        template = ["", "",
                    str_format % "Info",
                    str_format % "Low",
                    str_format % "Medium",
                    str_format % "High",
                    str_format % "Critical",
                    '-'*30,
                    str_format % "Total:"]
        atomclass = AtomShieldsScanner('/tmp')
        with Capturing() as output:
            atomclass.showSummary()
        for outputline, templateline in zip(output, template):
            assert templateline in outputline

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
