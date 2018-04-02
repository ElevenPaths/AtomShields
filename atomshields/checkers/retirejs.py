# -*- coding:utf8 -*-
from base import GenericChecker, checker
from atomshields import CommandHelper, Issue

import json, re, os
import requests
import tempfile
import shutil
from requests.exceptions import ConnectionError
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
		self.cache = {}

	@checker
	def run(self):
		"""
		"""
		if len(self.config['exclude_paths']) > 0:
			options = "--ignore {paths}".format(paths=','.join(self.config['exclude_paths']))
		else:
			options = ""


		self.scan(path = self.path, options = options, tempfile = False)

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
			if _links is not None and len(_links) > 0:
				jslinks[line] = _links

		old_path = os.getcwd()
		# Create tempdir and download JS
		for f in jslinks.keys():
			tmp_path = tempfile.mkdtemp(prefix="as_")
			for js in jslinks[f]:

				tmp_file = tempfile.mkstemp(dir=tmp_path, suffix=".js")[1]
				name = os.path.basename(tmp_file)
				self.download(js, tmp_file)
				self.cache[name] = js

			self.scan(path = tmp_path, options="", tempfile = True)





	def scan(self, path, options = "", tempfile = False):
		old_path = os.getcwd()
		os.chdir(path)
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

				# Check if is a tempfile and path should be replaced by URL
				if tempfile:
					issue.file = self.cache[os.path.basename(item["file"])]
				else:
					issue.file = item["file"].replace(self.path, "")
				issue.details = "{n} vulnerabilities found:\n".format(n=len(vulnerabilities))
				for v in vulnerabilities:
					if 'summary' in v['identifiers']:
						name = v['identifiers']['summary']
					elif 'CVE' in v['identifiers']:
						name = ','.join(v['identifiers']['CVE'])
					issue.details += "- {name}\n".format(name=name)

				updateTo = self.getLastVersion(component)
				if updateTo is not None:
					issue.details += "\nPlease, update to version {v}".format(v=updateTo)
				issue.severity = Issue.SEVERITY_MEDIUM
				issue.potential = False

				self.saveIssue(issue)
		except Exception as e:
			print "[!] Error: {e}".format(e=e)
		finally:
			os.chdir(old_path)
			if tempfile:
				shutil.rmtree(path)



	def download(self, url, path):
		try:
			r = requests.get(url, stream=True)
			with open(path, 'wb') as f:
				f.write(r.content)
		except ConnectionError:
			pass



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

		cmd = CommandHelper()
		cmd.install("nodejs-legacy")

		# Install retre with npm
		cmd = CommandHelper()
		cmd.command = "npm install -g retire"
		cmd.execute()

		if cmd.errors:
			from termcolor import colored
			print colored(cmd.errors, "red")
		else:
			print cmd.output





	def test(self):
		"""
		Check the dependences. 

		Returns:
			bool: True if all dependences are installed. False else.
		"""

		status =  GenericChecker.isInstalled("retire")
		return status

