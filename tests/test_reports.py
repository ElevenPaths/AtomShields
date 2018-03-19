# -*- coding:utf8 -*-
import pytest
import os
from atomshields.reports import *
from atomshields import Issue


class TestReports():

    @classmethod
    def setUpClass(cls):
        print("\nRunning unit tests for reports")


    #################################
    ###            Echo           ###
    #################################

    def test_EchoReport_init(self):
        report = EchoReport()
        assert report.CONFIG['enabled']

    # def test_EchoReport_run(self):
    #     report = EchoReport()
    #     report.issues = [Issue('Sample', '/tmp.ini', severity="Info",potential=True)]
    #     output = report.run()


    #################################
    ###            HTTP           ###
    #################################

    # def test_HttpReport_init(self):
    #     report = HttpReport()
    #     report.issues = [Issue('Sample', '/tmp.ini', severity="Info",potential=True)]
    #     assert not report.CONFIG['enabled']
