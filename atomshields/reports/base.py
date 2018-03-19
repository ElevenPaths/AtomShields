# -*- coding:utf8 -*-


class GenericReport(object):
	"""
	Class inherited by all reporting modules.
	"""

	def __init__(self, issues):
		"""
		Class constructor.

		Args:
			issues (list): List of `Issue` instances
		"""
		self._issues = []
		self.issues = issues

	@property 
	def issues(self):
		"""
		Getter for 'issues' property

		Returns:
			list: List of `Issue` instances
		"""
		return self._issues

	@issues.setter
	def issues(self, value):
		"""
		Setter for 'issues' property

		Args:
			value (list): List of `Issue` instances

		"""
		self._issues = value



