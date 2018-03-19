# -*- coding:utf8 -*-


class GenericReport(object):
	"""
	Class inherited by all reporting modules.
	"""

	def __init__(self, issues = None):
		"""
		Class constructor.

		Args:
			issues (list): List of `Issue` instances
		"""
		self._issues = []
		self._config = {}
		self._project = None
		self.issues = issues

	@property
	def issues(self):
		"""
		Getter for 'issues' property

		Returns:
			list: List of `Issue` instances
		"""
		if self._issues is None:
			return []
		return self._issues

	@issues.setter
	def issues(self, value):
		"""
		Setter for 'issues' property

		Args:
			value (list): List of `Issue` instances

		"""
		self._issues = value

	@property
	def config(self):
		"""
		Getter for 'config' property

		Returns:
			dict: Dictionary which contains the current values for this report config
		"""
		return self._config

	@config.setter
	def config(self, value):
		"""
		Setter for 'config' property

		Args:
			value (dict): Dictionary which contains the current values for this report config

		"""
		self._config = value

	@property
	def project(self):
		"""
		Getter for 'project' property

		Returns:
			str: Project's name
		"""
		return self._project

	@project.setter
	def project(self, value):
		"""
		Setter for 'project' property

		Args:
			value (str): Project's name

		"""
		self._project = value
