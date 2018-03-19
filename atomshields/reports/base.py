# -*- coding:utf8 -*-


class GenericReport(object):
	"""
	Class inherited by all reporting modules.
	"""

	def __init__(self, issues):
		self._issues = []
		self.issues = issues


	@property 
	def issues(self):
		return self._issues

	@issues.setter
	def issues(self, value):
		self._issues = value



