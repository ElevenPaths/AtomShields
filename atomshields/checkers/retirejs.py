# -*- coding:utf8 -*-
from base import GenericChecker, checker
from atomshields import CommandHelper, Issue

import json, re
import requests
from packaging import version

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

				updateTo = self.getLastVersion(component)
				if updateTo is not None:
					issue.details += "\nPlease, update to version {v}".format(v=updateTo)
				issue.severity = Issue.SEVERITY_MEDIUM
				issue.potential = False

				#@TODO: Extraer la info de los JS enlazados directamente en tags script

				self.saveIssue(issue)


			# Find JS in cloud
			regex = "script.*src.*http"
			command = """grep -rile "{regex}" "{path}" """.format(path = self.path, regex = regex)
			cmd = CommandHelper(command)
			cmd.execute()

			jslinks = {}
			lines = cmd.output.split("\n")
			for line in lines:
				if not line.startswith(self.path):
					continue

				_links = self.getJSLinks(line)
				if jslinks is not None and len(jslinks) > 0:
					jslinks[line] = _links



		except Exception as e:
			print e



	def getLastVersion(self, component):
		url1 = "https://rawgit.com/RetireJS/retire.js/master/repository/jsrepository.json"
		url2 = "https://rawgit.com/RetireJS/retire.js/master/repository/npmrepository.json"

		obj1 = {}
		obj2 = {}
		r = requests.get(url1)
		if r.status_code == 200:
			obj1 = r.json()

		r = requests.get(url2)
		if r.status_code == 200:
			obj2 = r.json()

		data = obj1.copy()
		data.update(obj2)


		versions = map(lambda x : x['below'], data[component]['vulnerabilities'])
		return max(versions)


	def getJSLinks(self, filepath):
		regex = r"<script\ *([^>]*)(src\ *=\ *('|\")(https?://.*)('|\"))"
		f = open(filepath, 'r')
		content = f.read()
		f.close()

		prog = re.compile(regex, flags = re.MULTILINE | re.IGNORECASE)
		matches = prog.finditer(content)
		matches_data = []
		matchNum = 0
		for _matchNum, match in enumerate(matches):
			matchNum += 1
			matches_data.append(match.group(4))

		return matches_data



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

