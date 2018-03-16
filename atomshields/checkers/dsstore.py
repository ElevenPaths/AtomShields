#!/usr/bin/env python
# -*- coding:utf8 -*-

from base import GenericChecker
from atomshields import Issue
import subprocess

class DSStoreChecker(GenericChecker):

	NAME = "dsstore"
	DESCRIPTION = """Busca y elimina los ficheros .DS_Store"""
	CONFIG = {
		"enabled": True,
		"remove": True,
		"exclude_paths": []
	}

	def __init__(self):
		super(DSStoreChecker, self).__init__()


	def run(self):
		"""
		Finds .DS_Store files into path
		"""
		try:
			print "Running DSStore"
			command = "find {path} -type f -name \".DS_Store\" ".format(path=self.path)
			output = subprocess.check_output(command, shell=True)
			files = output.split("\n")
			for f in files:
				issue = Issue()
				issue.name = "File .DS_Store detected"
				issue.potential = False
				issue.severity = Issue.SEVERITY_LOW
				# Get only relative path
				issue.file = f.replace(self.path, "")

				self.saveIssue(issue)

				return self.issues

		except Exception as e:
			print e
