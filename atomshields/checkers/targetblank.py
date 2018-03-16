#!/usr/bin/env python
# -*- coding:utf8 -*-

from base import *
from atomshields import Issue
import subprocess
import re

class TargetBlankChecker(GenericChecker):

	NAME = "targetblank"
	DESCRIPTION = """Detecta vulnerabilidades 'Target Blank' en ficheros HTML"""
	CONFIG = {
		"enabled": True,
		"exclude_paths": ["test/", "docs/"]
	}

	REGEX = ur"(<a (?=.*href=(['\"])(https?:)?\/\/.*?\2)(?!.*rel=(['\"])(.*\bnoopener\b.*\bnoreferrer\b.*|.*\bnoreferrer\b.*\bnoopener\b.*)\4)[^>]*target=(['\"]?)_blank\6[^>]*)(>)([^<]*)(<\/a>)?"

	def __init__(self):
		super(TargetBlankChecker, self).__init__()


	@checker
	def run(self):
		regex = "target.*_blank"
		command = """grep -rile "{regex}" "{path}" """.format(path=self.path, regex = regex)
		p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		output = p.communicate()[0]

		lines = output.split("\n")
		for line in lines:
			if not line.startswith(self.path):
				continue

			#line is the file which contains "target.*_blank"

			# get content
			f = open(line, 'r')
			content = f.read()
			f.close()


			prog = re.compile(TargetBlankChecker.REGEX, re.MULTILINE)
			matches = prog.finditer(content)
			matches_data = []
			matchNum = 0
			for _matchNum, match in enumerate(matches):
				matchNum += 1
				matches_data.append(match.group())

			if matchNum > 0:
				issue = Issue()
				issue.name = "Target _blank vulnerability"
				issue.file = line.replace(self.path, "")
				issue.severity = Issue.SEVERITY_MEDIUM
				details = ["""It has been found that your 'a' tags with attribute target="_blank" don't have the attribute rel="noopener", and this makes possible to carry out phishing attacks.""",
				"Lines affected:"] 
				details += matches_data
				issue.details = "\n".join(details)

				self.saveIssue(issue)
