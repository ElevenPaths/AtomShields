# -*- coding:utf8 -*-
import subprocess
from base import *
from atomshields import Issue

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


	@checker
	def run(self):
		"""
		Finds .DS_Store files into path
		"""
		filename = ".DS_Store"
		command = "find {path} -type f -name \"{filename}\" ".format(path = self.path, filename = filename)
		output = subprocess.check_output(command, shell = True)
		files = output.split("\n")
		for f in files:
			if not f.endswith(filename):
				continue

			issue = Issue()
			issue.name = "File .DS_Store detected"
			issue.potential = False
			issue.severity = Issue.SEVERITY_LOW

			# Get only relative path
			issue.file = f.replace(self.path, "")

			self.saveIssue(issue)
