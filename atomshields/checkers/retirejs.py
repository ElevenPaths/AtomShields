# -*- coding:utf8 -*-
from base import GenericChecker, checker
from atomshields import CommandHelper, Issue

import json

class RetireJSChecker(GenericChecker):

	NAME = "retirejs"
	DESCRIPTION = """Detecta ficheros JavaScript vulnerables"""
	CONFIG = {
		"enabled": True,
		"exclude_paths": ["test/"]
	}

	def __init__(self):
		super(RetireJSChecker, self).__init__()

	@checker
	def run(self):
		"""
		"""
		if len(self.config['exclude_paths']) > 0:
			options = "--ignore {paths}".format(paths=','.join(self.config['exclude_paths']))
		else:
			options = ""

		command = "retire --outputformat json --nocache {option} 2>&1".format(option=options)
		cmd = CommandHelper(command)
		cmd.execute()

		try:
			results = json.loads(cmd.output.strip())

			for item in results:
				component = item['results'][0]['component']
				version = item['results'][0]['version'] 

				vulnerabilities = item['results'][0]['vulnerabilities']

				issue = Issue(name = "Vulnerability in {c} v{v}".format(c=component, v=version))
				issue.file = item["file"].replace(self.path, "")
				issue.details = "{n} vulnerabilities found:\n".format(n=len(vulnerabilities))
				for v in vulnerabilities:
					issue.details += "- {name}\n".format(name=v['identifiers']['summary'])
				issue.severity = Issue.SEVERITY_MEDIUM
				issue.potential = False

				self.saveIssue(issue)



		except Exception as e:
			print e


	@staticmethod
	def install():
		"""
		Install all the dependences
		"""
		cmd = CommandHelper()
		cmd.install("npm")
		cmd.install("retire")



	def test(self):
		"""
		Check the dependences. 

		Returns:
			bool: True if all dependences are installed. False else.
		"""

		status =  GenericChecker.isInstalled("retire")
		return status

