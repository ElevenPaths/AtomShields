# -*- coding:utf8 -*-
import pytest
import os
import sys
from cStringIO import StringIO
from atomshields.reports.echo import *
from atomshields.reports.http import *
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

    def test_EchoReport_run(self):
        headers = '{:<40}  {:<20} {:<40}'.format("Vulnerability", "Severity", "File affected")
        results = '{:<40}  {:<20} {:<40}'.format("Sample", "INFO", '/tmp.ini')

        report = EchoReport()
        report.issues = [Issue('Sample', '/tmp.ini', severity="Info")]
        with Capturing() as output:
            report.run()
        assert headers in output
        assert results in output


    #################################
    ###            HTTP           ###
    #################################

    # def test_HttpReport_init(self):
    #     report = HttpReport()
    #     report.issues = [Issue('Sample', '/tmp.ini', severity="Info",potential=True)]
    #     assert not report.CONFIG['enabled']

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout
