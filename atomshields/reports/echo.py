#!/usr/bin/env python
# -*- coding:utf8 -*-

from reports.base import GenericReport
from termcolor import colored
from atomshields import Issue

class EchoReport(GenericReport):

	NAME = "echo"
	DESCRIPTION = """Muestra las vulnerabilidades por pantalla"""
	CONFIG = {
		"enabled": True,
	}
	
	def __init__(self):
		super(EchoReport, self).__init__()

	def run(self, issues):

		format_str = '{:<40}  {:<20} {:<40}'

		# Header
		print ""
		print format_str.format("Vulnerability", "Severity", "File affected")
		print "-"*80
		
		for issue in issues:
			print format_str.format(issue.name, issue.severity.upper(), issue.file)



	
